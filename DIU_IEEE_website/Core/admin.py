from django.contrib import admin
from .models import WebsiteSettings

@admin.register(WebsiteSettings)
class WebsiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'logo','contact_email', 'background_image', 'modified_date')
    ordering = ('modified_date',)
    
# Register your models here.
