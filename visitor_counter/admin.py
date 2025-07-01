from django.contrib import admin
from visitor_counter.models import VisitorCounter
from django.contrib.admin.sites import site

# Register your models here.
class VisitorCounterAdmin(admin.ModelAdmin):
    list_display=['count']


admin.site.register(VisitorCounter,VisitorCounterAdmin)
