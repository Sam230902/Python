from django.urls import path
from .views import userLogin, userLogout
from django.conf import settings
from django.conf.urls.static import static
from .views import *



urlpatterns = [
    path('login/', userLogin, name='login'),
    path('logout/', userLogout, name='logout'),
    path('home',home,name='Homepage'),
    path('sample',sample,name='Home'),
    path('contact',contact,name="Contact"),
    path("aadharList",aadharList,name="aadharList"),
    path("createAadhar",createAadhar,name="CreateForm"),
    path("updateAadhar/<int:id>",updateAadhar,name="updateForm"),
    path("deleteAadhar/<int:id>",deleteAadhar,name="delete")
    
   
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
