# app.py
import os
import threading
import json
from datetime import datetime

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from flask import Flask, request, make_response

HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", "9889"))
MODEL_PATH = os.getenv("MODEL_PATH", "model/skin_cancer_cnn.h5")

model = None
app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024

tf.get_logger().setLevel("ERROR")


def load_model():
    global model
    try:
        m = Sequential([
            Conv2D(32, (3, 3), activation="relu", input_shape=(224, 224, 3)), MaxPooling2D((2, 2)),
            Conv2D(64, (3, 3), activation="relu"), MaxPooling2D((2, 2)),
            Conv2D(128, (3, 3), activation="relu"), MaxPooling2D((2, 2)),
            Flatten(), Dense(512, activation="relu"), Dropout(0.5), Dense(1, activation="sigmoid")
        ])
        m.load_weights(MODEL_PATH)
        model = m
        print("[INFO] Model loaded")
    except Exception as e:
        print(f"[ERROR] Model load failed: {e}")


threading.Thread(target=load_model, daemon=True).start()


def base_ui_payload():
    return {
        "message": "Skin Cancer Prediction API Ready",
        "ui_text": {
            "resultBtn": "Analyze Image",
            "textEdit": "Upload dermoscopic image to analyze...",
            "probablityLabel": "Confidence",
            "timeLabel": "Timestamp"
        }
    }


def severity_bucket(prob):
    if prob < 0.5:
        return "Normal", "Findings are consistent with a benign-appearing lesion; no observable malignant features."
    if prob < 0.6:
        return "Initial", "Initial atypical melanocytic changes noted; correlate clinically."
    if prob < 0.7:
        return "Mild", "Mild malignant potential suggested. Consider short-interval follow-up."
    if prob < 0.8:
        return "Moderate", "Moderate malignant potential. Recommend dermoscopic evaluation."
    if prob < 0.9:
        return "High", "High malignant potential. Recommend urgent specialist review."
    return "Severe", "Severe malignant melanoma strongly suspected. Immediate evaluation warranted."


def json_reply(payload, status_code=200):
    resp = make_response(json.dumps(payload), status_code)
    resp.headers["Content-Type"] = "application/json"
    return resp


@app.route("/", methods=["GET"])
def root():
    p = base_ui_payload()
    p["log"] = {"type": "success", "message": "Connected to Skin AI"}
    return json_reply(p, 200)


@app.route("/predict", methods=["POST"])
def predict():
    global model
    if model is None:
        p = base_ui_payload()
        p.update({"error": "Model loading", "log": {"type": "verbose", "message": "Model still loading"}})
        return json_reply(p, 200)

    ct = request.headers.get("Content-Type", "")
    if not ct.lower().startswith("multipart/form-data"):
        p = base_ui_payload()
        p.update({"error": "multipart/form-data required", "log": {"type": "error", "message": "Missing boundary"}})
        return json_reply(p, 400)

    if "file" not in request.files:
        p = base_ui_payload()
        p.update({"error": "No 'file' field", "log": {"type": "error", "message": "file field missing"}})
        return json_reply(p, 400)

    try:
        img_bytes = request.files["file"].read()
        img = tf.io.decode_image(img_bytes, channels=3, expand_animations=False)
        img = tf.image.resize(tf.cast(img, tf.float32) / 255.0, [224, 224])
        x = tf.expand_dims(img, 0).numpy()

        prob = float(model.predict(x)[0][0])
        pct = f"{prob * 100:.2f}%"
        when = datetime.now().strftime("%H:%M %d %b %Y")
        label, desc = severity_bucket(prob)
        benign = prob < 0.5
        btn_text = "Benign" if benign else "Malignant"

        p = base_ui_payload()
        p["ui_text"]["resultBtn"] = btn_text
        p.update({
            "severity": label,
            "probability": ("Normal" if benign else pct),
            "description": desc,
            "time": when,
            "log": {"type": "success", "message": "Prediction complete"}
        })
        return json_reply(p, 200)
    except Exception as e:
        p = base_ui_payload()
        p.update({"error": f"Failed to process image: {e}", "log": {"type": "error", "message": "Processing failed"}})
        return json_reply(p, 500)


@app.errorhandler(404)
def not_found(_):
    p = base_ui_payload()
    p.update({"error": "Not Found", "log": {"type": "verbose", "message": "Route not found"}})
    return json_reply(p, 404)


@app.errorhandler(400)
def bad_request(_):
    p = base_ui_payload()
    p.update({"error": "Malformed request", "log": {"type": "error", "message": "Malformed request line"}})
    return json_reply(p, 400)


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, threaded=True, debug=False)
