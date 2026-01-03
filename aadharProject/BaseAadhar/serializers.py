from rest_framework.serializers import ModelSerializer
from .models import AadharUser

class AadharUserSerializer(ModelSerializer):
    class Meta:
        model=AadharUser
        fields="__all__"
        
        
    