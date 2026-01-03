from django.db import models

def upload_to(instance,filename):
    return f"{instance.AadharNumber}/{filename}"


class AadharUser(models.Model):
    AadharNumber = models.CharField(max_length=14, unique=True)
    FullName = models.CharField(max_length=10)
    PhoneNumber=models.CharField(max_length=10,unique=True)
    Date_Of_Birth = models.DateField()
    Gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    Address = models.TextField()
    Email = models.EmailField()
    Image = models.ImageField(upload_to=upload_to,null=True,blank=True)
    Created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.FullName} - {self.AadharNumber}"

