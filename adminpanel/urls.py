from django.urls import path
from .views import (
    admin_login,
    admin_dashboard,
    projects_list,
    student_detail,
    add_payment,
    
)

from .internship import(add_domain,add_duration,add_mode
                        ,update_domain,update_duration,update_mode,
                        delete_domain,delete_duration,delete_mode,
                        list_mode,list_duration,list_domain,
                        intern_list,internstudent_detail)


from .training import(training_list)


app_name='adminpanel'

urlpatterns = [
    path('company_admin/', admin_login, name='admin_login'),

    path('dashboard/', admin_dashboard, name='admin_dashboard'),

   

    path('student/<int:id>/', student_detail, name='student_detail'),

    path(
    'add-payment/<int:project_id>/',
      add_payment,
    name='add_payment'
),



    path("add_mode/",add_mode.as_view(),name="add_mode"),

    path("add_duration/",add_duration.as_view(),name="add_duration"),

    path("add_domain/",add_domain.as_view(),name="add_domain"),

     path("update_mode/<int:pk>/",update_mode.as_view(),name="update_mode"),

    path("update_duration/<int:pk>/",update_duration.as_view(),name="update_duration"),

    path("update_domain/<int:pk>/",update_domain.as_view(),name="update_domain"),


    path("delete_mode/<int:pk>/",delete_mode.as_view(),name="delete_mode"),

    path("delete_duration/<int:pk>/",delete_duration.as_view(),name="delete_duration"),

    path("delete_domain/<int:pk>/",delete_domain.as_view(),name="delete_domain"),


    path('list_mode/',list_mode.as_view(),name="list_mode"),

    path('list_duration/',list_duration.as_view(),name="list_duration"),

    path('list_domain/',list_domain.as_view(),name="list_domain"),

   
    path('internstudent_detail/<int:pk>',internstudent_detail.as_view(),name="internstudent_detail"),


    path('training_list/',training_list,name="training_list"),

    path('projects_list/',projects_list,name="projects_list"),

    path('internship_list/',intern_list,name="internship_list"),

    
       

]