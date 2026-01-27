# NetScryer

**Network Performance & SLA Intelligence Platform**  
SaaS tarzında çalışan, multi-lokasyon hız testi ve raporlama sistemi.  
Docker ile tek komutla çalıştırabilir, Web Panel ve API üzerinden verileri izleyebilirsin.

---

## 🚀 Özellikler

- Ping / Download / Upload ölçümü
- Multi-lokasyon agent desteği
- Backend: FastAPI
- Frontend: Web Panel (HTML/JS)
- Docker Compose ile kolay deploy
- Prometheus & Grafana destekli monitoring
- SLA raporlama ve PDF/CSV rapor
- Windows / Linux uyumlu
- Tek komutla çalıştırma (`run.sh`)

---

## 📦 Kurulum

### Ön Koşullar

- Docker / Docker Compose kurulu olmalı
- Windows: Docker Desktop
- Linux: `docker` ve `docker-compose` kurulu

### Adımlar

```bash
# Zip veya klasörü indir ve aç
cd netscryer

# Tek komutla başlat
bash run.sh




| Servis     | URL                                                      |
| ---------- | -------------------------------------------------------- |
| Web Panel  | [http://localhost](http://localhost)                     |
| API Docs   | [http://localhost:8000/docs](http://localhost:8000/docs) |
| Grafana    | [http://localhost:3000](http://localhost:3000)           |
| Prometheus | [http://localhost:9090](http://localhost:9090)           |




netscryer/
├── agent/
│   └── agent.py
├── backend/
│   ├── main.py
│   ├── auth.py
│   └── requirements.txt
├── frontend/
│   └── index.html
├── worker/
│   └── worker.py
├── reports/
│   └── report.py
├── infra/
│   ├── docker-compose.yml
│   └── prometheus.yml
├── .env.example
└── run.sh




