from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from Ornek.models import Student

def calculate_mean(students):
    total=0
    for student in students:
        total = total+student.FinalGrade
    return total/len(students)

def index(request):
    if request.user.is_authenticated:
        username= request.user.username
        students = Student.objetcts.all()
        mean=calculate_mean(students)
        return render(request,'index.html',{
            'username':username,
            'students':students,
            'mean': round(mean,2)
            })
            
    else:
        return redirect('/login')
    
def register(request):	
    if request.method =='POST':
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return redirect("/login")
    else:
        return render(request,'Register.html')



def login(request):
    if request.method =='POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/index")
        else:
            return render(request,'Login.html',{'Error':True})
    else:
        return render(request,'Login.html')

         
def logout(request):
    auth.logout(request)
    return  redirect("/login")
