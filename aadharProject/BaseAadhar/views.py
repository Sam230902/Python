from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import AadharUser
from .serializers import AadharUserSerializer

# Create your views here.
@api_view(["GET"])
def getAllAadhar(request):
    data=AadharUser.objects.all()
    SerializedData=AadharUserSerializer(data,many=True)
    return Response(data=SerializedData.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def getAadharByID(request,id):
    data = AadharUser.objects.filter(id=id).first()
    serializedData=AadharUserSerializer(data)
    return Response(data=serializedData.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def createAadhar(request):
    serializedData=AadharUserSerializer(data=request.data)
    if serializedData.is_valid():
        serializedData.save()
        return Response(data=serializedData.data, status=status.HTTP_201_CREATED)
    return Response(serializedData.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def updateAadhar(request,id):
    aadharUser=AadharUser.objects.get(id=id)
    if aadharUser:
        serializedData=AadharUserSerializer(aadharUser,data=request.data)
        if serializedData.is_valid():
          serializedData.save()
          return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(["DELETE"])
def deleteAadhar(request,id):
    data=AadharUser.objects.get(id=id)
    if data:
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_404_NOT_FOUND)



