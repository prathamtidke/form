from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from first.models import Details

def index(request):
    context = {'success' : False}
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        age = request.POST['age']
        location = request.POST['location']
        # print(firstname,lastname,age,location)
        dt = Details(Firstname = firstname,Lastname = lastname,Age = age,Location = location)
        dt.save()
        context = {'success': True}
    return render(request,'index.html',context)

def viewData(request):
    allDetail = Details.objects.all()
    # for item in allDetail:
    #     print(item.Firstname,item.Lastname,item.Age,item.Location)
    context = {'Details' : allDetail}
    return render (request,'viewData.html',context)
