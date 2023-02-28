from django.db import models
import secrets
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(null=True, blank=True)
	image_url = models.CharField(max_length=1000, null=True, blank=True)
	price = models.FloatField(null=True, blank=True)

	def __str__(self):
		return self.name

class Order(models.Model):
	product = models.ForeignKey(Product, max_length=200, null=True, blank=True, on_delete = models.SET_NULL)
	created =  models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		return self.product.name

class Ownerproduct(models.Model):
	ownername = models.CharField(max_length=200)
	ownerdescription = models.TextField(null=True, blank=True)
	ownerimage_url = models.CharField(max_length=1000, null=True, blank=True)
	ownerprice = models.FloatField(null=True, blank=True)

	def __str__(self):
		return self.ownername

class Ownerorder(models.Model):
	ownerproduct = models.ForeignKey(Ownerproduct, max_length=200, null=True, blank=True, on_delete = models.SET_NULL)
	ownercreated =  models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		return self.ownerproduct.ownername

class Learnerproduct(models.Model):
	learnername = models.CharField(max_length=200)
	learnerdescription = models.TextField(null=True, blank=True)
	learnerimage_url = models.CharField(max_length=1000, null=True, blank=True)
	learnerprice = models.FloatField(null=True, blank=True)

	def __str__(self):
		return self.learnername

class Learnerorder(models.Model):
	learnerproduct = models.ForeignKey(Learnerproduct, max_length=200, null=True, blank=True, on_delete = models.SET_NULL)
	learnercreated =  models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		return self.learnerproduct.learnername

class Licenseproduct(models.Model):
	licensename = models.CharField(max_length=200)
	licensedescription = models.TextField(null=True, blank=True)
	licenseimage_url = models.CharField(max_length=1000, null=True, blank=True)
	licenseprice = models.FloatField(null=True, blank=True)

	def __str__(self):
		return self.licensename

class Licenseorder(models.Model):
	licenseproduct = models.ForeignKey(Licenseproduct, max_length=200, null=True, blank=True, on_delete = models.SET_NULL)
	licensecreated =  models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		return self.licenseproduct.licensename



class posdetail(models.Model):
    posname=models.CharField(max_length=100)
    bvn=models.CharField(max_length=100)
    posemail=models.CharField(max_length=100)
    posaddress=models.CharField(max_length=100)
    posstate=models.CharField(max_length=100)
    
    # def __str__(self):
    #     return self.name

class changeofownerdetail(models.Model):
    old_fullname=models.CharField(max_length=100)
    old_dob=models.CharField(max_length=100)
    old_phone=models.CharField(max_length=100)
    old_email=models.CharField(max_length=100)
    old_address=models.CharField(max_length=200)
    old_state=models.CharField(max_length=200)
    # ----------------------------------------
    new_fullname=models.CharField(max_length=100)
    new_dob=models.CharField(max_length=100)
    new_phone=models.CharField(max_length=100)
    new_email=models.CharField(max_length=100)
    new_address=models.CharField(max_length=100)
    new_state=models.CharField(max_length=100)
    new_use=models.CharField(max_length=100)
    # -----------------------------------------
    change_make=models.CharField(max_length=100)
    change_model=models.CharField(max_length=100)
    change_colour=models.CharField(max_length=100)
    change_plate=models.CharField(max_length=100)
    change_chasis=models.CharField(max_length=100)
    change_engine=models.CharField(max_length=100)

class learnerpermitdetail(models.Model):
    learners_name=models.CharField(max_length=100)
    learners_dob=models.CharField(max_length=100)
    learners_phone=models.CharField(max_length=100)
    learners_email=models.CharField(max_length=100)
    learners_address=models.CharField(max_length=100)
    learners_state=models.CharField(max_length=100)
    learners_routes=models.CharField(max_length=100)

class renewaldetail(models.Model):
    license_name=models.CharField(max_length=100)
    license_dob=models.CharField(max_length=100)
    license_gender=models.CharField(max_length=100)
    license_phone=models.CharField(max_length=100)
    license_email=models.CharField(max_length=100)
    license_address=models.CharField(max_length=100)
    license_state=models.CharField(max_length=100)
    license_category=models.CharField(max_length=100)
    license_use=models.CharField(max_length=100)
    license_make=models.CharField(max_length=100)
    license_model=models.CharField(max_length=100)
    license_colour=models.CharField(max_length=100)
    license_makeyear=models.CharField(max_length=100)
    license_vehitype=models.CharField(max_length=100)
    license_plate=models.CharField(max_length=100)
    license_chasis=models.CharField(max_length=100)
    license_engine=models.CharField(max_length=100)


class CustomerInfo(models.Model):
    full_name= models.CharField(max_length  = 150)
    email_pay= models.EmailField()
    phone_number = models.CharField(max_length= 20)
    address = models.CharField(max_length = 150)

class Clientprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

