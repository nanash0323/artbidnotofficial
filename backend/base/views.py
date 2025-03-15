from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Sample product data (Replace with database later)
products = [
    {"_id": "1", "name": "Sunset Painting", "image": "/images/sunset.jpg", "price": 150},
    {"_id": "2", "name": "Abstract Art", "image": "/images/abstract.jpg", "price": 200},
    {"_id": "3", "name": "Portrait Sketch", "image": "/images/portrait.jpg", "price": 120},
]

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
