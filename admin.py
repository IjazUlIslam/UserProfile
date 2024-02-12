from django.contrib import admin
from UserProfile.models import CustomUser, DateTime


# Reigister CustomUser model and also display its field
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "phone_number", "upload_image"]


# register DateTime Model
@admin.register(DateTime)
class DateTimeAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_time', 'time_zone']
