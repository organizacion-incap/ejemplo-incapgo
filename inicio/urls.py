#
from django.urls import path
from . import views

app_name = "inicio_app"

urlpatterns = [
    #Certifications    
    path(
        '' ,
        views.Home.as_view(),
        name='index',
    ),  
    

]