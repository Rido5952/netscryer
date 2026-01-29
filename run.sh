#!/bin/bash
set -e
echo "🚀 NetScryer başlatılıyor..."
docker compose up -d --build
echo "✅ Panel: http://localhost"
echo "✅ API: http://localhost:8000/docs"
echo "✅ Grafana: http://localhost:3000"
