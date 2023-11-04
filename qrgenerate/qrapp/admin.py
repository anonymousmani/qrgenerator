from django.contrib import admin
from qrapp.models import qr
# Register your models here.


class hello(admin.ModelAdmin):
    list_display = ('name', 'text')
    
admin.site.register(qr, hello)
