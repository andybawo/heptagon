from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('changeofowner',views.changeofowner,name='changeofowner'),
    path('email_message',views.email_message,name='email_message'),
    path('contact',views.contact,name='contact'),
    path('learners',views.learners,name='learners'),
    path('license',views.license,name='license'),
    path('pos',views.pos,name='pos'),
	path('simple_checkout/', views.simpleCheckout, name="simple_checkout"),
    path('store/', views.store, name="store"),
    path('ownerstore/', views.ownerstore, name="ownerstore"),
    path('learnerstore/', views.learnerstore, name="learnerstore"),
    path('licensestore/', views.licensestore, name="licensestore"),
    path('checkout/<int:pk>/', views.checkout, name="checkout"),
    path('ownercheckout/<int:pk>/', views.ownercheckout, name="ownercheckout"),
    path('learnercheckout/<int:pk>/', views.learnercheckout, name="learnercheckout"),
    path('licensecheckout/<int:pk>/', views.licensecheckout, name="licensecheckout"),
    path('complete/', views.paymentComplete, name="complete"),
    path('ownercomplete/', views.OwnerpaymentComplete, name="ownercomplete"),
    path('learnercomplete/', views.LearnerpaymentComplete, name="learnercomplete"),
    path('licensecomplete/', views.LicensepaymentComplete, name="licensecomplete"),
    path('services',views.services,name='services'),
]