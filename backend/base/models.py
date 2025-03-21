from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(Group, related_name="customuser_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions_set", blank=True)

    def __str__(self):
        return self.username

class ArtUpload(models.Model):
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField()
    uploaded_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="art_uploads")

    def __str__(self):
        return f"{self.uploaded_by.username} - {self.description[:30]}"  # Show first 30 chars of description

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name