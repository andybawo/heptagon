from django.contrib import admin
from django.urls import path
from .views import *
from .import views

urlpatterns = [
    # path('',views.loginStaff,name='loginStaff'),
    # path('createaccount',views.createaccount,name='createaccount'),
    path('',views.signin,name='signin'),
    path('logout',views.logout,name='logout'),
    path('admin',views.admin,name='admin'),
    path('tables',views.tables,name='tables'),
    path('forms',views.forms,name='forms'),
    path('register',views.register,name='register'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('posform',views.posform,name='posform'),
    path('posstaff',views.posstaff,name='posstaff'),
    path('changestaff',views.changestaff,name='changestaff'),
    path('learnerstaff',views.learnerstaff,name='learnerstaff'),
    path('renewalstaff',views.renewalstaff,name='renewalstaff'),
    path('changeofownerform',views.changeofownerform,name='changeofownerform'),
    path('renewalform',views.renewalform,name='renewalform'),
    path('learnerspermitform',views.learnerspermitform,name='learnerspermitform'),
    path('update/<int:myid>/',update,name='update'),
    path('update1/<int:myid>/',update1,name='update1'),
    path('update2/<int:myid>/',update2,name='update2'),
    path('update3/<int:myid>/',update3,name='update3'),
    path('posstaff/<int:myid>/',posstaff,name='posstaff'),
    path('changestaff/<int:myid>/',changestaff,name='changestaff'),
    path('renewalstaff/<int:myid>/',renewalstaff,name='renewalstaff'),
    path('learnerstaff/<int:myid>/',learnerstaff,name='learnerstaff'),
    path('del_item/<int:myid>/',del_item,name='del_item'),
    path('posform_print',views.posform_print,name='posform_print'),
    path('change_print',views.change_print,name='change_print'),
    path('del_itemc/<int:myid>/',del_itemc,name='del_itemc'),
    path('del_itemr/<int:myid>/',del_itemr,name='del_itemr'),
    path('del_itemp/<int:myid>/',del_itemp,name='del_itemp'),
    path('viewall',viewall,name="viewall"),
    path('searchme',searchme,name="searchme"),
]
