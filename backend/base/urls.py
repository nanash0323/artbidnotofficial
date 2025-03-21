from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    RegisterView, LoginView, LogoutView,
    ProductList,  # ✅ Import ProductList
    upload_art
)

urlpatterns = [
    # ✅ Authentication Routes
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

    # ✅ Product API Routes
    path("products/", ProductList.as_view(), name="get-products"),  # Matches /api/products/

    # ✅ Image Upload Route
    path("upload/", upload_art, name="upload-art"),  # Matches /api/upload/
]

# ✅ Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
