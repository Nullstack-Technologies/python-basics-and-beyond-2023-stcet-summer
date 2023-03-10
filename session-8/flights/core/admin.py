from django.contrib import admin

from .models import Flight

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ['frm', 'to', 'date_time']
    search_fields = ['frm', 'to']
    list_filter = ['date_time']