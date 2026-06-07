"""Image processing endpoints (PDF Task 2).

multipart/form-data ile gelen "image" dosyasini isler:
  - POST /get/resolution      -> {"width": W, "height": H}
"""

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from PIL import Image


def _get_uploaded_image(request):
    """multipart/form-data 'image' alanindan yuklenen dosyayi dondurur (yoksa None)."""
    return request.FILES.get("image")


@csrf_exempt
@require_POST
def get_resolution(request):
    """Gelen gorselin cozunurlugunu (genislik x yukseklik) dondurur."""
    upload = _get_uploaded_image(request)
    if upload is None:
        return JsonResponse(
            {"error": "'image' alaninda bir dosya gonderin (multipart/form-data)."},
            status=400,
        )

    try:
        with Image.open(upload) as img:
            width, height = img.size
    except Exception:
        return JsonResponse(
            {"error": "Gecersiz veya bozuk gorsel dosyasi."},
            status=400,
        )

    return JsonResponse({"width": width, "height": height})
