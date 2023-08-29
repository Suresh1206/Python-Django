from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse
from .models import Student
# Create your views here.

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == "POST":
        id = request.POST['sid'].upper()
        name = request.POST['name'].upper()
        branch = request.POST['branch'].upper()
        if Student.objects.filter(Student_id=id).exists():
            messages.info(request,"Id Already Exist")
            return redirect('home')
        else:
            user = Student(Student_id=id,Student_Name=name,Student_Branch=branch)
            user.save()
            messages.info(request,"Registered Succesfully")
            return render(request,"home.html")
    else:
        return render(request,'home.html')

def loginpage(request):
    return render(request,'loginpage.html')

def login(request):
    if request.method=='POST':
        name = request.POST['name']
        password = request.POST['password']
        user = auth.authenticate(username=name,password=password)
        if user is not None:
            data = Student.objects.all().values()
            return render(request,"login.html",{"datas":data})
        else:
            messages.info(request,"Only Admin can login!")
            return redirect('home')
    else:
        return render(request,'loginpage.html')

def delete(request):
    if request.method=="POST":
        sid = request.POST['sid'].upper()
        if (Student.objects.filter(Student_id=sid).exists()):
            id = Student.objects.get(Student_id=sid)
            id.delete()
            messages.info(request,"Deleted Successfully")
            data = Student.objects.all().values()
            return render(request,"delete.html",{"datas":data})
        else:
            messages.info(request,"Id doesnot exist")
            return redirect('delete')
    else:
        data = Student.objects.all().values()
        return render(request,"delete.html",{"datas":data})


def update(request):
    if request.method=="POST":
        id1 = request.POST['id1'].upper()
        if Student.objects.filter(Student_id=id1).exists():
            id2=request.POST['id2'].upper()
            name = request.POST['name'].upper()
            branch = request.POST['branch'].upper()
            id = Student.objects.get(Student_id=id1)
            id.delete()
            user = Student(Student_id=id2,Student_Name=name,Student_Branch=branch)
            user.save()
            messages.info(request,"Updated Succesfully")
            return redirect('update')
        else:
            messages.info(request,"No such ID")
            return redirect('update') 
    else:
        data = Student.objects.all().values()
        return render(request,"update.html",{"datas":data})
        
