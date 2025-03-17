from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

# Sample product data (Replace with database later)
products = [
    {"_id": "1", "name": "Sunset Painting", "image": "/images/sunset.jpg", "price": 150},
    {"_id": "2", "name": "Abstract Art", "image": "/images/abstract.jpg", "price": 200},
    {"_id": "3", "name": "Portrait Sketch", "image": "/images/portrait.jpg", "price": 120},
]

# ✅ Generate JWT tokens for a user
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }

# ✅ Home Route
@api_view(['GET'])
def home(request):
    return Response({"message": "Welcome to the API. Go to /api/products/ to view products."})

# ✅ Get all products
@api_view(['GET'])
def getProducts(request):
    return Response({"products": products})  # Wrapped in an object for React compatibility

# ✅ Get a single product by ID
@api_view(['GET'])
def getProduct(request, pk):
    product = next((p for p in products if p["_id"] == pk), None)
    if product:
        return Response(product)
    return Response({"message": "Product not found"}, status=404)

# ✅ API routes list
@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/products/',
        '/api/products/<id>/',
        '/api/products/create/',
        '/api/products/upload/',
        '/api/products/<id>/reviews/',
        '/api/products/top/',
        '/api/products/delete/<id>/',
        '/api/products/update/<id>/',
        '/api/register/',
        '/api/login/',
        '/api/logout/',
    ]
    return Response(routes)

# ✅ Image Upload Endpoint
@csrf_exempt  # Use this for testing; enable CSRF protection in production
def upload_art(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        description = request.POST.get('description', '')

        # Save the file
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        file_url = fs.url(filename)

        # Return a success response
        return JsonResponse({
            'message': 'Upload successful',
            'file_url': file_url,
            'description': description
        })
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

# ✅ User Registration
@api_view(["POST"])
def register_user(request):
    """Handles user registration"""
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already taken"}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, email=email, password=password)
    return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)

# ✅ User Login
@api_view(["POST"])
def login_user(request):
    """Handles user login and token generation"""
    username = request.data.get("username")
    password = request.data.get("password")

    user = User.objects.filter(username=username).first()
    if user and user.check_password(password):
        tokens = get_tokens_for_user(user)
        return Response(tokens, status=status.HTTP_200_OK)
    
    return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

# ✅ User Logout
@api_view(["POST"])
def logout_user(request):
    """Handles logout by blacklisting the refresh token"""
    try:
        refresh_token = request.data.get("refresh_token")
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"message": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
    except Exception:
        return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
