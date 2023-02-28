from django.contrib import admin
from .models import *

# Register your models here.

from .models import Product, Order, Ownerproduct, Ownerorder, Learnerproduct, Learnerorder, Licenseproduct,Licenseorder, CustomerInfo, Clientprofile

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Ownerproduct)
admin.site.register(Ownerorder)
admin.site.register(Learnerproduct)
admin.site.register(Learnerorder)
admin.site.register(Licenseproduct)
admin.site.register(Licenseorder)
admin.site.register(CustomerInfo)
admin.site.register(Clientprofile)

class showposdetail(admin.ModelAdmin):
    list_display=('posname','bvn','posemail','posaddress','posstate')
admin.site.register(posdetail,showposdetail)

class showchangeofownerdetail(admin.ModelAdmin):
    list_display=('old_fullname','old_dob','old_phone','old_email','old_address','old_state','new_fullname','new_dob','new_phone','new_email','new_address','new_state','new_use','change_make','change_model','change_colour','change_plate','change_chasis','change_engine')
admin.site.register(changeofownerdetail,showchangeofownerdetail)

class showlearnerpermitdetail(admin.ModelAdmin):
    list_display=('learners_name','learners_dob','learners_phone','learners_email','learners_address','learners_state','learners_routes')
admin.site.register(learnerpermitdetail,showlearnerpermitdetail)

class showrenewaldetail(admin.ModelAdmin):
    list_display=('license_name','license_dob','license_gender','license_phone','license_email','license_address','license_state','license_category','license_use','license_make','license_model','license_colour','license_makeyear','license_vehitype','license_plate','license_chasis','license_engine')
admin.site.register(renewaldetail,showrenewaldetail)