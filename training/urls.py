from django.urls import path

from .views import project_register, payment_page,razorpay_payment,offline_payment

app_name='training'


urlpatterns = [
    path('project_register/', project_register, name='project_register'),
  
    path('payment/<int:project_id>/', payment_page, name='payment_page'),

    path('razorpay/<int:payment_id>/', razorpay_payment, name='razorpay_payment'),


    path('offline/<int:payment_id>/', offline_payment, name='offline_payment'),


]