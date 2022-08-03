from pyexpat import model
from django.contrib import admin
from .models import registration

# Register your models here.
@admin.register(registration)
class modeladmin(admin.ModelAdmin):
    list_display=('id','name','email','address')
