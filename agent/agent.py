import socket, time, requests
def ping(): 
    s=socket.socket(); t=time.time()
    try: s.connect(("8.8.8.8",53))
    except: return 999
    s.close(); return round((time.time()-t)*1000,2)
payload = {"ping": ping(), "download": 100, "upload": 20}
try:
    requests.post("http://localhost:8000/api/report", json=payload)
except Exception as e:
    print("Agent error:", e)
