from django.urls import path

from .views import project_register, team_members, payment_page,razorpay_payment,offline_payment,home_page

app_name='projects'

urlpatterns = [
    path('project_register/', project_register, name='project_register'),

    path('team-members/<int:project_id>/', team_members, name='team_members'),

    path('payment/<int:project_id>/', payment_page, name='payment_page'),

    path('razorpay/<int:payment_id>/', razorpay_payment, name='razorpay_payment'),

    path('offline/<int:payment_id>/', offline_payment, name='offline_payment'),

    path('home_page/',home_page,name='home_page'),
]