from email import message
from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return str(self.name)

class Career(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(null=True,blank=True)
    position= models.CharField(max_length=200)
    file = models.FileField(upload_to="resume") 

    def __str__(self):
        return str(self.name)