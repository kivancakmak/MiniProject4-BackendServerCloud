# Oracle Cloud x86 (AMD) Micro VM hedefi.
# DAIMA linux/amd64 icin build et:  docker build --platform linux/amd64 ...
# (ARM makinede bile amd64 imaj uretmek icin build komutundaki --platform bayragini kullan.)
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Sadece runtime bagimliliklari (django, pillow, gunicorn).
# requirements-dev.txt (ruff, pre-commit) imaja GIRMEZ.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Proje dosyalari (.dockerignore ile gereksizler haric).
COPY . .

# Container icinde 8000 dinlenir.
EXPOSE 8000

# Production WSGI sunucusu (dev runserver degil).
CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2"]
