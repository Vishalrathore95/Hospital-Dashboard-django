from django.contrib import admin


from .models import HealthCareStats

class HealthCareStatsAdmin(admin.ModelAdmin):
    list_display = ('category', 'count')
    # Customize other admin options as needed

admin.site.register(HealthCareStats, HealthCareStatsAdmin)

