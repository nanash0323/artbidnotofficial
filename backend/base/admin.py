from django.contrib import admin
from .models import CustomUser, ArtUpload

admin.site.register(CustomUser)
admin.site.register(ArtUpload)
