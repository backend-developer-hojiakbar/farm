from django.contrib import admin
from .models import FarmerHome
# Register your models here.
@admin.register(FarmerHome)
class FarmerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
