from django.db import models

# Create your models here.
class login(models.Model):
    createname=models.CharField(max_length=100)
    createemail=models.CharField(max_length=100)
    createusername=models.CharField(max_length=50)
    createpassword=models.CharField(max_length=50)

class posapproval(models.Model):
    approved = models.BooleanField('Aprroved', default=False)

