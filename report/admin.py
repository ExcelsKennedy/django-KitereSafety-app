from django.contrib import admin
from .models import PhotoReport

# Register your models here.
# admin.site.register(PhotoReport) 

@admin.register(PhotoReport)
class PhotoReportAdmin(admin.ModelAdmin):
    list_display=PhotoReport.DisplayFields
    list_filter=PhotoReport.FilterFields 