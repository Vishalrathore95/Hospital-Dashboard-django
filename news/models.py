from django.db import models
from tinymce.models import HTMLField

class news(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title}: {self.content}"
    
