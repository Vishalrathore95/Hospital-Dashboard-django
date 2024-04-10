from django.contrib import admin
from .models import Doctor

# @admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'specialization', 'qualification', 'hospital', 'contact_number', 'date_of_birth', 'gender', 'years_of_experience')
    search_fields = ('full_name', 'email', 'hospital')
    list_filter = ('specialization', 'qualification', 'gender')
    ordering = ('full_name', 'date_of_birth')
admin.site.register(Doctor, DoctorAdmin)


