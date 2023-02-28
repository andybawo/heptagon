from email import message
from http.client import HTTPResponse
from multiprocessing import context
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from re import template
from django.shortcuts import render,redirect
from .models import *
from django.core.mail import send_mail
from client.forms import SignUpForm
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.db.models import Count
from django.http import JsonResponse
import json


from .forms import CustomerInfoForm

# Create your views here.

def customer_info(request):
    if request.method == 'POST':
       customer_form = CustomerInfoForm(request.method)
    if customer_form.is_valid()and customer_form.cleaned_data:
       customer_form.save()
       return render (request, 'users/payment.html',{'email_pay':customer_form.email})
    else:
       return HTTPResponse('Invalid input try again!!!')






def index(request):
    return render(request, 'users/index.html')   

def about(request):
    return render(request, 'users/about.html')

def email_message(request):
    return render(request, 'users/email_message.html')
                    
def changeofowner(request):
    if request.method=='POST':
        oldname= request.POST['old_fullname']
        olddob= request.POST['old_dob']
        oldphone= request.POST['old_phone']
        oldemail= request.POST['old_email']
        oldaddress= request.POST['old_address']
        oldstate= request.POST['old_state']
                        # ------------------------------------
        newname= request.POST['new_fullname']
        newdob= request.POST['new_dob']
        newphone= request.POST['new_phone']
        newemail= request.POST['new_email']
        newaddress= request.POST['new_address']
        newstate= request.POST['new_state']
        newuse= request.POST['new_use']
                        # ------------------------------------
        changemake= request.POST['change_make']
        changemodel= request.POST['change_model']
        changecolour= request.POST['change_colour']
        changeplate= request.POST['change_plate']
        changechasis= request.POST['change_chasis']
        changeengine= request.POST['change_engine']
        savedata=changeofownerdetail(old_fullname=oldname,old_dob=olddob,old_phone=oldphone,old_email=oldemail,old_address=oldaddress,old_state=oldstate,new_fullname=newname,new_dob=newdob,new_phone=newphone,new_email=newemail,new_address=newaddress,new_state=newstate,new_use=newuse,change_make=changemake,change_model=changemodel,change_colour=changecolour,change_plate=changeplate,change_chasis=changechasis,change_engine=changeengine)
        savedata.save()
        return redirect('ownerstore')
    else:
        pass
        changeofownerform=changeofownerdetail.objects.all()
        context={
                'changeofownerform' : changeofownerform
            }
        return render(request, 'users/changeofowner.html',context)   

def contact(request):
    return render(request, 'users/contact.html')  

                #Checkout payment
                #==============================================================================

def simpleCheckout(request):
    return render(request, 'users/simple_checkout.html')  

def checkout(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product':product}
    return render(request, 'users/checkout.html', context)

def store(request,):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'users/store.html', context)

def paymentComplete(request):
    body = json.loads(request.body)
    print('BODY:', body)
    product = Product.objects.get(id=body['productId'])
    Order.objects.create(
        product=product
    )
    return JsonResponse('Payment completed!', safe=False)

def ownerstore(request,):
    ownerproducts = Ownerproduct.objects.all()
    context = {'ownerproducts':ownerproducts}
    return render(request, 'users/ownerstore.html', context)

def ownercheckout(request, pk):
    ownerproduct = Ownerproduct.objects.get(id=pk)
    context = {'ownerproduct':ownerproduct}
    return render(request, 'users/ownercheckout.html', context)

def OwnerpaymentComplete(request):
    body = json.loads(request.body)
    print('BODY:', body)
    ownerproduct = Ownerproduct.objects.get(id=body['ownerproductId'])
    Ownerorder.objects.create(
        ownerproduct=ownerproduct
    )
    return JsonResponse('Payment completed!', safe=False)

@login_required
def learnerstore(request,):
    learnerproducts = Learnerproduct.objects.all()
    context = {'learnerproducts':learnerproducts}
    return render(request, 'users/learnerstore.html', context)

def learnercheckout(request, pk):
    learnerproduct = Learnerproduct.objects.get(id=pk)
    context = {'learnerproduct':learnerproduct}
    return render(request, 'users/learnercheckout.html', context)

def LearnerpaymentComplete(request):
    body = json.loads(request.body)
    print('BODY:', body)
    learnerproduct = Learnerproduct.objects.get(id=body['learnerproductId'])
    Learnerorder.objects.create(
        learnerproduct=learnerproduct
    )
    return JsonResponse('Payment completed!', safe=False)

def licensestore(request,):
    licenseproducts = Licenseproduct.objects.all()
    context = {'licenseproducts':licenseproducts}
    return render(request, 'users/licensestore.html', context)

def licensecheckout(request, pk):
    licenseproduct = Licenseproduct.objects.get(id=pk)
    context = {'licenseproduct':licenseproduct}
    return render(request, 'users/licensecheckout.html', context)

def LicensepaymentComplete(request):
    body = json.loads(request.body)
    print('BODY:', body)
    licenseproduct = Licenseproduct.objects.get(id=body['licenseproductId'])
    Licenseorder.objects.create(
        licenseproduct=licenseproduct
    )
    return JsonResponse('Payment completed!', safe=False)

def learners(request):
    if request.method=='POST':
        learnersname= request.POST['learners_name']
        learnersdob= request.POST['learners_dob']
        learnersphone= request.POST['learners_phone']
        learnersemail= request.POST['learners_email']
        learnersaddress= request.POST['learners_address']
        learnersstate= request.POST['learners_state']
        learnersroutes= request.POST['learners_routes']
        savedata=learnerpermitdetail(learners_name=learnersname,learners_dob=learnersdob,learners_phone=learnersphone,learners_email=learnersemail,learners_address=learnersaddress,learners_state=learnersstate,learners_routes=learnersroutes)
        savedata.save()
        return redirect('signup')
    else:
        pass
        learnerspermitform=learnerpermitdetail.objects.all()
        context={
                'learnerspermitform' : learnerspermitform
        }
        return render(request, 'users/learners.html',context)   

def license(request):
    if request.method=='POST':
        licensename= request.POST['license_name']
        licensedob= request.POST['license_dob']
        licensegender= request.POST['license_gender']
        licensephone= request.POST['license_phone']
        licenseemail= request.POST['license_email']
        licenseaddress= request.POST['license_address']
        licensestate= request.POST['license_state']
        licensecategory= request.POST['license_category']
        licenseuse= request.POST['license_use']
                        # ---------------------------------------
        licensemake= request.POST['license_make']
        licensemodel= request.POST['license_model']
        licensecolour= request.POST['license_colour']
        licensemakeyear= request.POST['license_makeyear']
        licensevehitype= request.POST['license_vehitype']
        licenseplate= request.POST['license_plate']
        licensechasis= request.POST['license_chasis']
        licenseengine= request.POST['license_engine']
        savedata=renewaldetail(license_name=licensename,license_dob=licensedob,license_gender=licensegender,license_phone=licensephone,license_email=licenseemail,license_address=licenseaddress,license_state=licensestate,license_category=licensecategory,license_use=licenseuse,license_make=licensemake,license_model=licensemodel,license_colour=licensecolour,license_makeyear=licensemakeyear,license_vehitype=licensevehitype,license_plate=licenseplate,license_chasis=licensechasis,license_engine=licenseengine,)
        savedata.save()
        return redirect('licensestore')
    else:
        pass
        renewalform=renewaldetail.objects.all()
        context={
                'renewalform' : renewalform
            }
        return render(request, 'users/license.html',context)   

def pos(request):

    if request.method=='POST':
        namepos= request.POST['posname']
        bvnpos= request.POST['bvn']
        emailpos= request.POST['posemail']
        addresspos= request.POST['posaddress']
        statepos= request.POST['posstate']
        savedata=posdetail(posname=namepos,bvn=bvnpos,posemail=emailpos,posaddress=addresspos,posstate=statepos)
        savedata.save()
        return redirect('store')
    else:
        pass
                        
        posform=posdetail.objects.all()
        context={
                'posform' : posform
                }
        return render(request, 'users/pos.html',context)  




def services(request):
    return render(request, 'users/services.html')   

@login_required
def myaccount(request):
    return render(request, 'users/myaccount.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            userprofile = Clientprofile.objects.create(user=user)

            return redirect('services')
    else:
        form = SignUpForm()

    return render(request, 'users/signup.html', {
        'form': form
    })
