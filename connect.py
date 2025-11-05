import requests,os,json
from PyQt5.QtCore import QThread,pyqtSignal
class ConnectAPI(QThread):
    connectionResult=pyqtSignal(bool,dict)
    def __init__(self,host,port):
        super().__init__();self.host=(host or "").strip();self.port=(str(port) or "").strip();self.base_url=f"http://{self.host}:{self.port}"
    def run(self):
        try:
            r=requests.get(self.base_url,timeout=3);print(f"[ConnectAPI] {r.status_code}");print(r.text)
            if r.status_code==200:
                try:data=r.json()
                except: data={}
                if "ui_text"not in data:data["ui_text"]={"resultBtn":"Analyze Image","textEdit":"Upload dermoscopic image to analyze...","probablityLabel":"Confidence","timeLabel":"Response Time"}
                if "log"not in data:data["log"]={"type":"success","message":data.get("message","Connected")}
                data["_base_url"]=self.base_url;self.connectionResult.emit(True,data);return
        except Exception as e:
            print(f"[ConnectAPI]{e}")
        self.connectionResult.emit(False,{"_base_url":getattr(self,"base_url",None),"log":{"type":"error","message":"Connection failed"}})
class PredictAPI(QThread):
    predictResult=pyqtSignal(bool,dict)
    def __init__(self,base_url,file_path):
        super().__init__();self.base_url=base_url.rstrip("/");self.file_path=file_path
    def run(self):
        try:
            if not os.path.isfile(self.file_path):print("[PredictAPI] file not found");self.predictResult.emit(False,{"log":{"type":"error","message":"File not found"}});return
            with open(self.file_path,"rb") as f:r=requests.post(self.base_url+"/predict",files={"file":(os.path.basename(self.file_path),f,"application/octet-stream")},timeout=60)
            print(f"[PredictAPI] {r.status_code}");print(r.text)
            try:data=r.json()
            except: data={"raw":r.text}
            data["_status"]=r.status_code
            if r.status_code==200:self.predictResult.emit(True,data);return
            self.predictResult.emit(False,data);return
        except Exception as e:
            print(f"[PredictAPI]{e}");self.predictResult.emit(False,{"log":{"type":"error","message":str(e)}})
