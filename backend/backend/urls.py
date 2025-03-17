from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to the API. Go to /api/products/ to view products."})

urlpatterns = [
    path('', home),  # Root URL response
    path('admin/', admin.site.urls),  # Admin panel
    path('api/', include('base.urls')),  # API endpoints including authentication and products
    path('api/auth/', include('base.urls')),  # Authentication endpoints (register, login, logout)
]
