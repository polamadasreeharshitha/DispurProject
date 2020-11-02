from django.contrib import admin
from .models import Customer

class customerAdmin(admin.ModelAdmin):
    list_display=['Name','Address','Email','Contact','Status','Date']

admin.site.register(Customer,customerAdmin)
