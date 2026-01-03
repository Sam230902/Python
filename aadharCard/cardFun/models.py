from django.db import models

class AadharUser(models.Model):
    full_name = models.CharField(max_length=100)
    aadhar_number = models.CharField(max_length=12, unique=True)
    date_of_birth = models.DateField()
    address = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.full_name} ({self.aadhar_number})"