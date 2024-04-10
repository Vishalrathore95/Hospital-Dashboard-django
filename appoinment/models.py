from django.db import models

class AppointmentRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    doctor_choices = [
        ('dr-smith', 'Dr. Smith'),
        ('dr-jones', 'Dr. Jones'),
        ('dr-wilson', 'Dr. Wilson'),
        ('dr-miller', 'Dr. Miller'),
        ('dr-anderson', 'Dr. Anderson'),
        ('dr-brown', 'Dr. Brown'),
        ('dr-davis', 'Dr. Davis'),
        ('dr-evans', 'Dr. Evans'),
        ('dr-garcia', 'Dr. Garcia'),
        ('dr-hall', 'Dr. Hall'),
        ('dr-jackson', 'Dr. Jackson'),
        ('dr-kelly', 'Dr. Kelly'),
        ('dr-lee', 'Dr. Lee'),
        ('dr-martin', 'Dr. Martin'),
        ('dr-nelson', 'Dr. Nelson'),
        ('dr-owens', 'Dr. Owens'),
        ('dr-patel', 'Dr. Patel'),
        ('dr-ross', 'Dr. Ross'),
        ('dr-taylor', 'Dr. Taylor'),
        ('dr-white', 'Dr. White'),
    ]
    doctor = models.CharField(max_length=20, choices=doctor_choices)
    date_and_time = models.DateTimeField()

    def __str__(self):
        return f"{self.name} - {self.get_doctor_display()} - {self.date_and_time.strftime('%Y-%m-%d %H:%M')}"
