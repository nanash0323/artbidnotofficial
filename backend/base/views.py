from django.contrib.auth import authenticate
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, ArtUploadSerializer, ProductSerializer
from .models import ArtUpload, Product

# ✅ User Registration
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ✅ User Login
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            })
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

# ✅ User Logout (Handled on frontend)
class LogoutView(APIView):
    def post(self, request):
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)

# ✅ Get All Products
class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# ✅ Art Upload (CSRF exempt for testing; Enable CSRF in production)
@csrf_exempt  
def upload_art(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        description = request.POST.get('description', '')

        # Save the file
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        file_url = fs.url(filename)

        # Save to the database
        art = ArtUpload.objects.create(
            image=filename,
            description=description,
            uploaded_by=request.user
        )

        return JsonResponse({
            'message': 'Upload successful',
            'file_url': file_url,
            'description': description
        })
    
    return JsonResponse({'error': 'Invalid request'}, status=400)
