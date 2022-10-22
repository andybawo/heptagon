from multiprocessing import context
from operator import delitem
from django.shortcuts import render,redirect
from client.models import*
from django.contrib import messages
from client.views import pos
from .models import *

# PDF==============================
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
#+++++++++++++++++++++++++++++++++++++++++++++++++++
def posform_print(request):
    #create bytestream buffer
    buf = io.BytesIO()
    #create canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    #create text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica",14)
    #Add text
    #lines =[
     #   "Line 1",
    #    "Line 2",
     #   "Line 3",
      #  "Line 4",
    #]
    #Loop
    pos = posdetail.objects.all()

    lines = []
    
    for pospdf in pos:
        lines.append(pospdf.posname)
        lines.append(pospdf.bvn)
        lines.append(pospdf.posemail)
        lines.append(pospdf.posaddress)
        lines.append(pospdf.posstate)
        lines.append("  ")


    for line in lines:
        textob.textLine(line)

    #end
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)


    #return
    return FileResponse(buf, as_attachment=True, filename='pos.pdf')

#================================================================================
def change_print(request):
    #create bytestream buffer
    buf = io.BytesIO()
    #create canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    #create text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica",14)
    #Add text
    #lines =[
     #   "Line 1",
    #    "Line 2",
     #   "Line 3",
      #  "Line 4",
    #]
    #Loop
    change = changeofownerdetail.objects.all()

    lines = []
    
    for changepdf in change:
        lines.append(changepdf.old_fullname)
        lines.append(changepdf.old_dob)
        lines.append(changepdf.old_phone)
        lines.append(changepdf.old_email)
        lines.append(changepdf.old_address)
        lines.append(changepdf.old_state)
        lines.append(changepdf.new_fullname)
        lines.append(changepdf.new_dob)
        lines.append(changepdf.new_phone)
        lines.append(changepdf.new_email)
        lines.append(changepdf.new_address)
        lines.append(changepdf.new_state)
        lines.append(changepdf.new_use)
        lines.append(changepdf.change_make)
        lines.append(changepdf.change_model)
        lines.append(changepdf.change_colour)
        lines.append(changepdf.change_plate)
        lines.append(changepdf.change_chasis)
        lines.append(changepdf.change_engine)
        lines.append("  ")


    for line in lines:
        textob.textLine(line)

    #end
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)


    #return
    return FileResponse(buf, as_attachment=True, filename='change.pdf')


def admin_approval(request):
    return redirect(request, 'staff/admin_approval.html')       

# Create your views here.
def dashboard(request):
    return render(request, 'staff/dashboard.html') 



 

def admin(request):
    posform_count = posdetail.objects.count()
    change_count = changeofownerdetail.objects.count()
    learners_count = learnerpermitdetail.objects.count()
    license_count = renewaldetail.objects.count()
    pos_order = Order.objects.count()
    owner_order = Ownerorder.objects.count()
    license_order = Licenseorder.objects.count()    
    learner_order = Learnerorder.objects.count()
    context = {
        'posform_count':posform_count,
        'change_count':change_count,
        'learners_count':learners_count,
        'license_count':license_count,
        'pos_order':pos_order,
        'owner_order':owner_order,
        'license_order':license_order,
        'learner_order':learner_order,
    }
    return render(request, 'staff/admin.html',context)

def tables(request):
    return render(request, 'staff/tables.html') 

def forms(request):
    return render(request, 'staff/forms.html') 

def register(request):
    if request.method=='POST':
        fullname= request.POST['createname']
        email= request.POST['createemail']
        username= request.POST['createusername']
        password= request.POST['createpassword']
        savedata=login(createname=fullname,createemail=email,createusername=username,createpassword=password)
        savedata.save()  
        return redirect('signin') 
    else:
        pass
    return render(request, 'staff/register.html') 

def signin(request):
    if request.method=="POST":
        try:
            UserDetails=login.objects.get(createusername=request.POST['createusername'],createpassword=request.POST['createpassword'])
            request.session['createname']=UserDetails.createname
            request.session['id']=UserDetails.id
            return render(request,'staff/admin.html')
        except login.DoesNotExist as e:
            messages.success(request,'username or password invalid')
    return render(request, 'staff/signin.html')    

# def loginStaff(request):
#     if request.method=="POST":
#         try:
#             UserDetails=login.objects.get(createusername=request.POST['createusername'],createpassword=request.POST['createpassword'])
#             request.session['createname']=UserDetails.createname
#             request.session['id']=UserDetails.id
#             return render(request,'staff/dashboard.html')
#         except login.DoesNotExist as e:
#             messages.success(request,'username or password invalid')
#     return render(request, 'staff/loginStaff.html')

def logout(request):
    return render(request,'staff/signin.html')

# def createaccount(request):
#     if request.method=='POST':
#         fullname= request.POST['createname']
#         email= request.POST['createemail']
#         username= request.POST['createusername']
#         password= request.POST['createpassword']
#         savedata=login(createname=fullname,createemail=email,createusername=username,createpassword=password)
#         savedata.save()  
#         return redirect('signin') 
#     else:
#         pass
           
#     return render(request,'staff/createaccount.html',)  

def learnerstaff(request):
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
        return redirect('learnerspermitform')
    else:
        pass
        learnerspermitform=learnerpermitdetail.objects.all()
        log=login.objects.all()

        context={
            'learnerspermitform' : learnerspermitform,
            'log':log
        }
    return render(request, 'staff/learnerstaff.html', context) 

def learnerspermitform(request):
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
        return redirect('learnerspermitform')
    else:
        pass
        learnerspermitform=learnerpermitdetail.objects.all()
        log=login.objects.all()

        context={
            'learnerspermitform' : learnerspermitform,
            'log':log
        }
    return render(request, 'staff/learnerspermitform.html',context) 

def del_itemp(request,myid):
    delitem=learnerpermitdetail.objects.get(id=myid)
    delitem.delete()
    messages.info(request,'Deleted')
    return redirect('learnerspermitform')

def learnerstaff(request,myid):
    updateitem=learnerpermitdetail.objects.get(id=myid)
    learnerspermitform=learnerpermitdetail.objects.all()
    context={
        'updateitem':updateitem,
        'learnerspermitform':learnerspermitform,
    }
    return render(request,'staff/learnerstaff.html',context)

def update3(request,myid):
    upitem=learnerpermitdetail.objects.get(id=myid)
    upitem.learners_name=request.POST['learners_name']
    upitem.learners_dob=request.POST['learners_dob']
    upitem.learners_phone=request.POST['learners_phone']
    upitem.learners_email=request.POST['learners_email']
    upitem.learners_address=request.POST['learners_address']
    upitem.learners_state=request.POST['learners_state']
    upitem.learners_routes=request.POST['learners_routes']
    upitem.save()
    messages.info(request,'Item Updated Successfully!')
    return redirect('learnerspermitform')

def searchme(request):
    if request.method=='POST':
        iten = request.POST['search']
        learnerspermitform=learnerpermitdetail.objects.filter(learners_name=iten,learners_email=iten)
        context={
        'learnerspermitform' : learnerspermitform    
        }
        return render(request,'staff/learnerspermitform.html',context)
    else:
        pass
        learnerspermitform=learnerpermitdetail.objects.all()
        context={
        'learnerspermitform' : learnerspermitform
        }
        return render(request,'staff/learnerspermitform.html',context)

def viewall(request):
    if request.methods=='POST':
        iten = request.POST['view']
        learnerspermitform=learnerpermitdetail.objects.filter(learners_name=iten,learners_email=iten)
        context={
        'learnerspermitform' : learnerspermitform    
        }
        return render(request,'staff/learnerspermitform.html',context)
    else:
        pass
        learnerspermitform=learnerpermitdetail.objects.all()
        context={
        'learnerspermitform' : learnerspermitform
        }
        return render(request,'staff/learnerspermitform.html',context)
# ==================================================================================
# ==================================================================================
def renewalform(request):
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
        return redirect('renewalform')
    else:
        pass
        renewalform=renewaldetail.objects.all()
        log=login.objects.all()

        context={
            'renewalform' : renewalform,
            'log':log,
        }
    return render(request, 'staff/renewalform.html',context) 

def renewalstaff(request):
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
        return redirect('renewalform')
    else:
        pass
        renewalform=renewaldetail.objects.all()
        log=login.objects.all()

        context={
            'renewalform' : renewalform,
            'log':log,
        }
    return render(request, 'staff/renewalstaff.html',context)  

def del_itemr(request,myid):
    delitem=renewaldetail.objects.get(id=myid)
    delitem.delete()
    messages.info(request,'Deleted')
    return redirect('renewalform')

def renewalstaff(request,myid):
    updateitem=renewaldetail.objects.get(id=myid)
    renewalform=renewaldetail.objects.all()
    context={
        'updateitem':updateitem,
        'renewalform':renewalform,
    }
    return render(request,'staff/renewalstaff.html',context)


def update2(request,myid):
    upitem=renewaldetail.objects.get(id=myid)
    upitem.license_name=request.POST['license_name']
    upitem.license_dob=request.POST['license_dob']
    upitem.license_gender=request.POST['license_gender']
    upitem.license_phone=request.POST['license_phone']
    upitem.license_email=request.POST['license_email']
    upitem.license_address=request.POST['license_address']
    upitem.license_state=request.POST['license_state']
    upitem.license_category=request.POST['license_category']
    upitem.license_use=request.POST['license_use']
    # -----------------------------------------
    upitem.license_make=request.POST['license_make']
    upitem.license_model=request.POST['license_model']
    upitem.license_colour=request.POST['license_colour']
    upitem.license_makeyear=request.POST['license_makeyear']
    upitem.license_vehitype=request.POST['license_vehitype']
    upitem.license_plate=request.POST['license_plate']
    upitem.license_chasis=request.POST['license_chasis']
    upitem.license_engine=request.POST['license_engine']
    upitem.save()
    messages.info(request,'Item Updated Successfully!')
    return redirect('renewalform')

def searchme(request):
    if request.method=='POST':
        iten = request.POST['search']
        renewalform=renewaldetail.objects.filter(license_name=iten,license_email=iten)
        context={
        'renewalform' : renewalform    
        }
        return render(request,'staff/renewalform.html',context)
    else:
        pass
        renewalform=renewaldetail.objects.all()
        context={
        'renewalform' : renewalform
        }
        return render(request,'staff/renewalform.html',context)


def viewall(request):
    if request.methods=='POST':
        iten = request.POST['view']
        renewalform=renewaldetail.objects.filter(license_name=iten,license_email=iten)
        context={
        'renewalform' : renewalform    
        }
        return render(request,'staff/renewalform.html',context)
    else:
        pass
        renewalform=renewaldetail.objects.all()
        context={
        'renewalform' : renewalform
        }
        return render(request,'staff/renewalform.html',context)

# ===============================================================================================
# =================================================================================================

def changestaff(request):
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
        return redirect('changeofownerform')
    else:
        pass
        changeofownerform=changeofownerdetail.objects.all()
        log=login.objects.all()

        context={
            'changeofownerform' : changeofownerform,
            'log':log,
        }
    return render(request, 'staff/changestaff.html', context) 

def changeofownerform(request):
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
        return redirect('changeofownerform')
    else:
        pass
        changeofownerform=changeofownerdetail.objects.all()
        log=login.objects.all()

        context={
            'changeofownerform' : changeofownerform,
            'log':log,
        }
    return render(request, 'staff/changeofownerform.html',context)  

def del_itemc(request,myid):
    delitem=changeofownerdetail.objects.get(id=myid)
    delitem.delete()
    messages.info(request,'Deleted')
    return redirect('changeofownerform')

def changestaff(request,myid):
    updateitem=changeofownerdetail.objects.get(id=myid)
    changeofownerform=changeofownerdetail.objects.all()
    context={
        'updateitem':updateitem,
        'changeofownerform':changeofownerform,
    }
    return render(request,'staff/changestaff.html',context)


def update1(request,myid):
    upitem=changeofownerdetail.objects.get(id=myid)
    upitem.old_fullname=request.POST['old_fullname']
    upitem.old_dob=request.POST['old_dob']
    upitem.old_phone=request.POST['old_phone']
    upitem.old_email=request.POST['old_email']
    upitem.old_address=request.POST['old_address']
    upitem.old_state=request.POST['old_state']
    upitem.new_fullname=request.POST['new_fullname']
    upitem.new_dob=request.POST['new_dob']
    upitem.new_phone=request.POST['new_phone']
    upitem.new_email=request.POST['new_email']
    upitem.new_address=request.POST['new_address']
    upitem.new_state=request.POST['new_state']
    upitem.new_use=request.POST['new_use']
    upitem.change_make=request.POST['change_make']
    upitem.change_model=request.POST['change_model']
    upitem.change_colour=request.POST['change_colour']
    upitem.change_plate=request.POST['change_plate']
    upitem.change_chasis=request.POST['change_chasis']
    upitem.change_engine=request.POST['change_engine']
    upitem.save()
    messages.info(request,'Item Updated Successfully!')
    return redirect('changeofownerform')

def searchme(request):
    if request.method=='POST':
        iten = request.POST['search']
        changeofownerform=changeofownerdetail.objects.filter(new_fullname=iten,old_fullname=iten)
        context={
        'changeofownerform' : changeofownerform    
        }
        return render(request,'staff/changeofownerform.html',context)
    else:
        pass
        changeofownerform=changeofownerdetail.objects.all()
        context={
        'changeofownerform' : changeofownerform
        }
        return render(request,'staff/changeofownerform.html',context)


def viewall(request):
    if request.methods=='POST':
        iten = request.POST['view']
        changeofownerform=changeofownerdetail.objects.filter(new_fullname=iten,old_fullname=iten)
        context={
        'changeofownerform' : changeofownerform    
        }
        return render(request,'staff/changeofownerform.html',context)
    else:
        pass
        changeofownerform=changeofownerdetail.objects.all()
        context={
        'changeofownerform' : changeofownerform
        }
        return render(request,'staff/changeofownerform.html',context)

# =============================================================================================
# =============================================================================================
def posform(request):
    if request.method=='POST':
        namepos= request.POST['posname']
        bvnpos= request.POST['bvn']
        emailpos= request.POST['posemail']
        addresspos= request.POST['posaddress']
        statepos= request.POST['posstate']
        savedata=posdetail(posname=namepos,bvn=bvnpos,posemail=emailpos,posaddress=addresspos,posstate=statepos)
        savedata.save()
        return redirect('posform')
    else:
        pass
        posform=posdetail.objects.all()
        log=login.objects.all()

        context={
            'posform' : posform,
            'log':log,
        }
    return render(request, 'staff/posform.html',context,)   

def del_item(request,myid):
    delitem=posdetail.objects.get(id=myid)
    delitem.delete()
    messages.info(request,'Deleted')
    return redirect('posform')

def posstaff(request):
    if request.method=='POST':
        namepos= request.POST['posname']
        bvnpos= request.POST['bvn']
        emailpos= request.POST['posemail']
        addresspos= request.POST['posaddress']
        statepos= request.POST['posstate']
        savedata=posdetail(posname=namepos,bvn=bvnpos,posemail=emailpos,posaddress=addresspos,posstate=statepos)
        savedata.save()
        return redirect('posform')
    else:
        pass
        posform=posdetail.objects.all()
        log=login.objects.all()

        context={
            'posform' : posform,
            'log':log,
        }
    return render(request, 'staff/posstaff.html', context)

def posstaff(request,myid):
    updateitem=posdetail.objects.get(id=myid)
    posform=posdetail.objects.all()
    context={
        'updateitem':updateitem,
        'posform':posform,
    }
    return render(request,'staff/posstaff.html',context)


def update(request,myid):
    upitem=posdetail.objects.get(id=myid)
    upitem.posname=request.POST['posname']
    upitem.bvn=request.POST['bvn']
    upitem.posemail=request.POST['posemail']
    upitem.posaddress=request.POST['posaddress']
    upitem.posstate=request.POST['posstate']
    upitem.save()
    messages.info(request,'Item Updated Successfully!')
    return redirect('posform')

def searchme(request):
    if request.method=='POST':
        iten = request.POST['search']
        posform=posdetail.objects.filter(posname=iten,posemail=iten)
        context={
        'posform' : posform    
        }
        return render(request,'staff/posform.html',context)
    else:
        pass
        posform=posdetail.objects.all()
        context={
        'posform' : posform
        }
        return render(request,'staff/posform.html',context)


def viewall(request):
    if request.methods=='POST':
        iten = request.POST['view']
        posform=posdetail.objects.filter(posname=iten,posemail=iten)
        context={
        'posform' : posform    
        }
        return render(request,'staff/posform.html',context)
    else:
        pass
        posform=posdetail.objects.all()
        context={
        'posform' : posform
        }
        return render(request,'staff/posform.html',context)
# ==============================================================
# ===============================================================