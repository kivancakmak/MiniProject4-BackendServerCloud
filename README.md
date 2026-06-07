# backend-cloud — Image Processing API (Backend Server 2)

RoboMunch Mini-Project-4, PDF Task 2. Saf Django (DRF yok) + Pillow ile gorsel isleme.

## Endpoint'ler

Ikisi de `multipart/form-data` ile `image` alaninda bir dosya bekler.

| Method | Yol | Aciklama | Cevap |
|--------|-----|----------|-------|
| POST | `/get/resolution` | Gorselin cozunurlugu | `{"width": W, "height": H}` |
| POST | `/convert/grayscale` | Gri tonlamaya cevirir | `image/png` (bytes) |

Hata: gorsel yok/bozuk → `400` + `{"error": "..."}`. POST disi method → `405`.

## Yerelde calistirma

```bash
python -m venv venv
venv\Scripts\activate            # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8001
```

### Hizli test (curl)

```bash
curl -X POST -F "image=@test.png" http://127.0.0.1:8001/get/resolution
curl -X POST -F "image=@test.png" http://127.0.0.1:8001/convert/grayscale --output gray.png
```

## Notlar / Guvenlik

- `ALLOWED_HOSTS = ['*']` ve `DEBUG = True` su an YERELDE test + ileride VM IP'si icin acik.
  Production'a/buluta cikmadan once `ALLOWED_HOSTS`'u gercek alan adi/IP ile sinirla ve `DEBUG = False` yap.
- Endpoint'ler dis istemciden (Flutter) cagrildigi icin `@csrf_exempt` kullaniyor.
- `gunicorn` requirements'a eklendi; ileride Docker/cloud adiminda kullanilacak (dev sunucusu degil).

> Docker / CI-CD / cloud deployment sonraki adimlarda eklenecek.
