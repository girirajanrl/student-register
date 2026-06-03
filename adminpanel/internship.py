from django.shortcuts import render, redirect,get_object_or_404

from internship.models import StudentIntern,Payment,Duration_add,Domain,Intership_mode



from internship.forms import StudentInternForm, PaymentForm

from internship.forms import modeform,Durationform,Domainform

from django.urls import reverse_lazy

from django.views.generic import (

    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView

)




class add_mode(CreateView):

   model=Intership_mode #connect table

   form_class=modeform  #connect form

   template_name='adminpanel/internship/add_mode.html'  #connect template

   success_url=reverse_lazy("adminpanel:add_mode")  # navigate the page


class add_duration(CreateView):

   model=Duration_add

   form_class=Durationform

   template_name='adminpanel/internship/add_duration.html'

   success_url=reverse_lazy("adminpanel:add_duration")



class add_domain(CreateView):
   
   model=Domain

   form_class=Domainform

   template_name='adminpanel/internship/add_domain.html'

   success_url=reverse_lazy("adminpanel:add_domain")


class update_mode(UpdateView):
   
   model=Intership_mode

   form_class=modeform

   template_name="adminpanel/internship/add_mode.html"

   success_url = reverse_lazy(
        "adminpanel:list_mode"
    )


   
class update_duration(UpdateView):
   
   model=Duration_add

   form_class=Durationform

   template_name="adminpanel/internship/add_duration.html"

   success_url = reverse_lazy(
        "adminpanel:list_duration"
    )



class update_domain(UpdateView):
   
   model=Domain

   form_class=Domainform

   template_name="adminpanel/internship/add_domain.html"

   success_url = reverse_lazy(
        "adminpanel:list_domain"
    )



class delete_mode(DeleteView):  
   
   model=Intership_mode


   template_name="adminpanel/internship/delete_mode.html"

   success_url = reverse_lazy(
        "adminpanel:list_mode"
    )

   
class delete_duration(DeleteView):
   
   model=Duration_add


   template_name="adminpanel/internship/delete_duration.html"

   success_url = reverse_lazy(
        "adminpanel:list_duration"
    )


class delete_domain(DeleteView):
   
   model=Domain


   template_name="adminpanel/internship/delete_domain.html"

   success_url = reverse_lazy(
        "adminpanel:list_domain"
    )


class list_mode(ListView):
   
   model=Intership_mode

   context_object_name="modes"

   template_name="adminpanel/internship/list_mode.html"


class list_duration(ListView):
   
   model=Duration_add

   context_object_name="durations"

   template_name="adminpanel/internship/list_duration.html"

class list_domain(ListView):
   
   model=Domain
   
   context_object_name="domains"

   template_name="adminpanel/internship/list_domain.html"


class internship_list(ListView):
   
   model=StudentIntern

   template_name='adminpanel/register_list/internship_list.html'

   context_object_name="students"


class internstudent_detail(DetailView):
   

   model=StudentIntern

   context_object_name="student"

   template_name="adminpanel/internship/internstudentdetail.html"


def intern_list(request):

   total_count=StudentIntern.objects.count()

   list_interns=StudentIntern.objects.all()

   return render(request,"adminpanel/register_list/internship_list.html",{'total_count':total_count,'list_interns':list_interns})


