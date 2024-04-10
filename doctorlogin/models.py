from django.db import models

class Doctor(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    specialization = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    hospital = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    date_of_birth = models.DateField(blank=True, null=True)  
    years_of_experience = models.IntegerField()
    profile_picture = models.ImageField(upload_to='profile_pictures/', max_length=500, null=True, default=None)# Field name

    def __str__(self):
        return self.full_name



