from datetime import date
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests as req
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from django.shortcuts import render, redirect
from django.contrib import messages

base_url="http://127.0.0.1:5554/"


def userLogin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("aadharList") 
        else:
            messages.error(request, "Invalid username or password")
    
    return render(request, "login.html")

def userLogout(request):
    logout(request)
    return redirect("login")

def home(request):
    return render(request, "home.html")

def sample(request):
    return render(request,"sample.html")
 
def contact(request):
    return render(request,"contact.html") 

def aadharList(request):
    data = req.get(base_url+"Base/getAllAadhar")
    return render(request, "aadharList.html", {"list":data.json()})

def createAadhar(request):
    if request.method == "GET":
        aadharForm = AadharForm()
        return render(request, "aadharForm.html", {"forms":aadharForm})
    elif request.method == "POST":
        aadharData = AadharForm(request.POST,request.FILES)
        if aadharData.is_valid():
            jsonData = aadharData.cleaned_data
            for key, value in jsonData.items():
                if isinstance(value, date):
                    jsonData[key] = value.isoformat()
            image_file = request.FILES.get("Image")
            data = {key: str(value) for key, value in jsonData.items() if key != "Image"}  
            files = {"Image": image_file} if image_file else {}     
            try:
                res = req.post(base_url + "Base/createAadhar", data=data, files=files)
                if res.status_code == 201:
                    messages.success(request, "Aadhar registration successful!")
                    return redirect("aadharList")
                else:
                    messages.error(request, f"API Error: {res.text}")
                    return render(request, "aadharForm.html", {"form": aadharData})
            except req.exceptions.RequestException as e:
                messages.error(request, f"Request failed: {str(e)}")
                return render(request, "aadharForm.html", {"form": aadharData})

        messages.error(request, "Form submission failed. Please check the fields.")
        return render(request, "aadharForm.html", {"form": aadharData})


def updateAadhar(request, id):
    if request.method == "GET":
        try:
            response = req.get(base_url + f"Base/getAadharByID/{id}")
            if response.status_code == 200:
                jsonData = response.json()
                aadharForm = AadharForm(initial=jsonData)
                return render(request, "aadharForm.html", {"forms": aadharForm})
            else:
                messages.error(request, "Failed to fetch Aadhar details.")
                return redirect("aadharList")
        except req.exceptions.RequestException as e:
            messages.error(request, f"Request failed: {str(e)}")
            return redirect("aadharList")
    elif request.method == "POST":
        aadharData = AadharForm(request.POST, request.FILES)
        if aadharData.is_valid():
            jsonData = aadharData.cleaned_data
            for key, value in jsonData.items():
                if isinstance(value, date):
                    jsonData[key] = value.isoformat()
            image_file = request.FILES.get("Image")
            data = {key: str(value) for key, value in jsonData.items() if key != "Image"}
            files = {"Image": (image_file.name, image_file, image_file.content_type)} if image_file else {}
            try:
                res = req.put(base_url + f"Base/updateAadharID/{id}", data=data, files=files)
                if res.status_code == 200 or res.status_code == 201:
                    messages.success(request, "Aadhar details updated successfully!")
                    return redirect("aadharList")
                else:
                    messages.error(request, f"API Error: {res.text}")
                    return render(request, "aadharForm.html", {"form": aadharData})

            except req.exceptions.RequestException as e:
                messages.error(request, f"Request failed: {str(e)}")
                return render(request, "aadharForm.html", {"form": aadharData})

        messages.error(request, "Form submission failed. Please check the fields.")
        return render(request, "aadharForm.html", {"form": aadharData})
            

def deleteAadhar(request, id):
    if request.method == "POST":
        res = req.delete(base_url+f"Base/deleteAadhar/{id}")
        print(res.text)
        if res.status_code == 204:
            return redirect("aadharList")
        else:
            return HttpResponse(f"API Error: {res.status_code}")


      












