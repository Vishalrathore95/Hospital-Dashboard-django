from django.db import models

from django.db import models

class HealthCareStats(models.Model):
    category = models.CharField(max_length=100)
    count = models.IntegerField()

    def __str__(self):
        return f"{self.category}: {self.count}"

