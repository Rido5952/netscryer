from fastapi import FastAPI
from pydantic import BaseModel
import time
app = FastAPI(title="NetScryer API")
class Speed(BaseModel):
    ping: float
    download: float
    upload: float
DATA=[]
@app.post("/api/report")
def report(s: Speed):
    DATA.append({"ts": time.time(), **s.dict()})
    return {"status": "ok"}
@app.get("/api/latest")
def latest():
    return DATA[-1] if DATA else {}
