from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    # Avoid reverse accessor conflicts
    groups = models.ManyToManyField(Group, related_name="custom_users", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_users", blank=True)

    def __str__(self):
        return self.username

class ArtUpload(models.Model):
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField()
    uploaded_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="art_uploads")

    def __str__(self):
        return f"{self.uploaded_by.username} - {self.description[:30]}"  # Show first 30 chars of the description
