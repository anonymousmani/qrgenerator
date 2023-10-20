from django.contrib import admin
from qrapp.models import qr
# Register your models here.


@admin.register(qr)
class hello(admin.ModelAdmin):
    list_display = ('name', 'text')