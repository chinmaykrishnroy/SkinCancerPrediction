import socket,threading,io,json,re
from datetime import datetime
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Flatten,Dense,Dropout

HOST,PORT,MODEL_PATH,BUF="127.0.0.1",8000,"model/skin_cancer_cnn.h5",4096
model=None

def load_model():
    global model
    try:
        model=Sequential([
            Conv2D(32,(3,3),activation='relu',input_shape=(224,224,3)),MaxPooling2D((2,2)),
            Conv2D(64,(3,3),activation='relu'),MaxPooling2D((2,2)),
            Conv2D(128,(3,3),activation='relu'),MaxPooling2D((2,2)),
            Flatten(),Dense(512,activation='relu'),Dropout(0.5),Dense(1,activation='sigmoid')
        ])
        model.load_weights(MODEL_PATH)
        print("[INFO] Model loaded")
    except Exception as e:
        print(f"[ERROR] Model load failed: {e}")

threading.Thread(target=load_model,daemon=True).start()

def base_ui_payload():
    return {
        "message":"Skin Cancer Prediction API Ready",
        "ui_text":{
            "resultBtn":"Analyze Image",
            "textEdit":"Upload dermoscopic image to analyze...",
            "probablityLabel":"Confidence",
            "timeLabel":"Timestamp"
        }
    }

def parse_multipart(data,boundary):
    files={}
    for p in data.split(b"--"+boundary.encode()):
        if b'Content-Disposition' in p:
            if b"\r\n\r\n" not in p: continue
            h,c=p.split(b"\r\n\r\n",1); c=c.rstrip(b"\r\n--")
            m=re.search(b'name="([^"]+)"',h)
            if m: files[m.group(1).decode()]=c
    return files

def jsend(conn,code,payload):
    body=json.dumps(payload).encode()
    conn.sendall(f"HTTP/1.1 {code}\r\nContent-Type: application/json\r\nContent-Length: {len(body)}\r\n\r\n".encode()+body)

def severity_bucket(prob):
    if prob<0.5: return "Normal","Findings are consistent with a benign-appearing lesion; no observable malignant features."
    if prob<0.6: return "Initial","Initial atypical melanocytic changes noted; correlate clinically."
    if prob<0.7: return "Mild","Mild malignant potential suggested. Consider short-interval follow-up."
    if prob<0.8: return "Moderate","Moderate malignant potential. Recommend dermoscopic evaluation."
    if prob<0.9: return "High","High malignant potential. Recommend urgent specialist review."
    return "Severe","Severe malignant melanoma strongly suspected. Immediate evaluation warranted."

def handle_client(conn,addr):
    global model
    print(f"[INFO] Connection from {addr}")
    try:
        data=b""
        while True:
            ch=conn.recv(BUF)
            if not ch: break
            data+=ch
            if b"\r\n\r\n" in data: break
        if not data: return
        hs_end=data.find(b"\r\n\r\n")
        headers,body=data[:hs_end].decode(errors="ignore"),data[hs_end+4:]
        line=headers.split("\r\n")[0]
        try:
            method,path,_=line.split()
        except:
            p=base_ui_payload();p.update({"error":"Malformed request","log":{"type":"error","message":"Malformed request line"}})
            jsend(conn,"400 Bad Request",p); return

        if method=="GET" and path=="/":
            p=base_ui_payload();p["log"]={"type":"success","message":"Connected to Skin AI"}
            jsend(conn,"200 OK",p); return

        bmatch=re.search(r"Content-Type:\s*multipart/form-data;\s*boundary=([^\r\n;]+)",headers,re.I)
        boundary=bmatch.group(1) if bmatch else None

        if method=="POST" and path=="/predict":
            if model is None:
                p=base_ui_payload();p.update({"error":"Model loading","log":{"type":"verbose","message":"Model still loading"}})
                jsend(conn,"200 OK",p); return
            if not boundary:
                p=base_ui_payload();p.update({"error":"multipart/form-data required","log":{"type":"error","message":"Missing boundary"}})
                jsend(conn,"400 Bad Request",p); return
            clm=re.search(r"Content-Length:\s*(\d+)",headers,re.I)
            if clm:
                need=int(clm.group(1))
                while len(body)<need:
                    ch=conn.recv(BUF)
                    if not ch: break
                    body+=ch
            files=parse_multipart(body,boundary)
            if "file" not in files:
                p=base_ui_payload();p.update({"error":"No 'file' field","log":{"type":"error","message":"file field missing"}})
                jsend(conn,"400 Bad Request",p); return
            try:
                img_bytes=files["file"]
                img=tf.io.decode_image(img_bytes,channels=3,expand_animations=False)
                img=tf.image.resize(tf.cast(img,tf.float32)/255.0,[224,224])
                x=tf.expand_dims(img,0).numpy()
                prob=float(model.predict(x)[0][0])
                pct=f"{prob*100:.2f}%"
                when=datetime.now().strftime("%H:%M %d %b %Y")
                label,desc=severity_bucket(prob)
                benign=prob<0.5
                btn_text="Benign" if benign else "Malignant"
                p=base_ui_payload()
                p["ui_text"]["resultBtn"]=btn_text
                p.update({
                    "severity":label,                                  # one-word/phrase label
                    "probability":("No Malignancy detected" if benign else pct),
                    "description":desc,
                    "time":when,
                    "log":{"type":"success","message":"Prediction complete"}
                })
                jsend(conn,"200 OK",p)
            except Exception as e:
                p=base_ui_payload();p.update({"error":f"Failed to process image: {e}","log":{"type":"error","message":"Processing failed"}})
                jsend(conn,"500 Internal Server Error",p)
            return

        p=base_ui_payload();p.update({"error":"Not Found","log":{"type":"verbose","message":"Route not found"}})
        jsend(conn,"404 Not Found",p)
    except Exception as e:
        print(f"[ERROR] Client failed: {e}")
    finally:
        conn.close(); print(f"[INFO] Connection closed: {addr}")

def run_server():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM); s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind((HOST,PORT)); s.listen(5)
    print(f"[INFO] Server listening at http://{HOST}:{PORT}")
    while True:
        conn,addr=s.accept()
        threading.Thread(target=handle_client,args=(conn,addr),daemon=True).start()

if __name__=="__main__": run_server()
