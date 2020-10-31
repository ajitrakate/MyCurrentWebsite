from django.contrib import admin
from .models import Profile, Board_required, Button_required

# Register your models here.
admin.site.register(Profile)
admin.site.register(Board_required)
admin.site.register(Button_required)
