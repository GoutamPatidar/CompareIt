from django.contrib import admin
from .models import profile_data, UserHistory


# Register your models here.
admin.site.register(profile_data)
admin.site.register(UserHistory)
