from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path("getAllAadhar",getAllAadhar,name="AllAadhar"),
    path("createAadhar",createAadhar,name="newAadhar"),
    path("getAadharByID/<int:id>",getAadharByID,name="getID"),
    path("updateAadharID/<int:id>",updateAadhar,name="updateAadhar"),
    path("deleteAadhar/<int:id>",deleteAadhar,name="deleteAadhar")
    
   
    
   
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

