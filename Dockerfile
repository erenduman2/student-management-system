# Base image
FROM python:3.10-slim

# Çalışma dizini oluştur
WORKDIR /app

# Gereksinim dosyasını kopyala
COPY requirements.txt .

# PostgreSQL geliştirme araçlarını yükle
RUN apt-get update && apt-get install -y libpq-dev gcc

# Bağımlılıkları yükle
RUN pip install --no-cache-dir -r requirements.txt

# Tüm kodu kopyala
COPY . .

# API'yi çalıştırma
#CMD ["python", "app.py"]
CMD ["uvicorn", "src.api.routes:app", "--host", "0.0.0.0", "--port", "8000"]
