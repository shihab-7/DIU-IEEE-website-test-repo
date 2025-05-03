from django.contrib import admin
from .models import Event
# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title','description', 'event_date', 'location', 'created_at', 'image']
    search_fields = ['title',]
    list_filter = ['event_date',]
    ordering = ['-event_date',]

