from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, ArtUpload

# ✅ Custom User Admin
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')

admin.site.register(CustomUser, CustomUserAdmin)

# ✅ Register Art Uploads
admin.site.register(ArtUpload)
