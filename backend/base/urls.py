from django.urls import path
from .views import (
    register_user, login_user, logout_user,
    getProducts, getProduct, getRoutes, upload_art
)

urlpatterns = [
    # ✅ Authentication Routes
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),

    # ✅ API Routes
    path("routes/", getRoutes, name="api-routes"),  # Matches /api/routes/
    path("products/", getProducts, name="get-products"),  # Matches /api/products/
    path("products/<str:pk>/", getProduct, name="get-product"),  # Matches /api/products/1/
    
    # ✅ Image Upload Route
    path("upload/", upload_art, name="upload-art"),  # Matches /api/upload/
]
