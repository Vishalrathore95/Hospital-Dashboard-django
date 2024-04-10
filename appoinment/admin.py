from django.contrib import admin
from appoinment.models import AppointmentRequest

class AppointmentRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'doctor', 'date_and_time')
    search_fields = ('name', 'email', 'doctor')
    list_filter = ('doctor', 'date_and_time')

admin.site.register(AppointmentRequest, AppointmentRequestAdmin)
