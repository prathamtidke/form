from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['Last Name']
        age = request.POST['Age']
        location = request.POST['Location']
        print(first_name,lastname,age,location)
    return render(request,'index.html')

def viewData(request):
    return render (request,'viewData.html')
