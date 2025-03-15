from django.urls import path
from .views import getProducts, getProduct, getRoutes, upload_art

urlpatterns = [
    path('routes/', getRoutes, name="api-routes"),  # Matches /api/routes/
    path('products/', getProducts, name="get-products"),  # Matches /api/products/
    path('products/<str:pk>/', getProduct, name="get-product"),  # Matches /api/products/1/
    path('upload/', upload_art, name='upload-art'),  # Matches /api/upload/
]
