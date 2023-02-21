from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Place
from django.contrib.auth.models import User
from django.contrib import messages,auth
# Create your views here.
def demo(request):
     obj=Place.objects.all()
     return render(request,"index.html",{'result':obj})
# def addition(request):
#      n1=int(request.GET["num1"])
#      n2=int(request.GET["num2"])
#      res=n1+n2
#      return render(request,"result.html",{'result':res})
def register(request):
     if request.method=='POST':
          username=request.POST['username']
          first_name = request.POST['first_name']
          last_name = request.POST['last_name']
          email = request.POST['email']
          password = request.POST['password']
          cpassword = request.POST['password1']
          if password==cpassword:
               if User.objects.filter(username=username).exists():
                    messages.info(request,"username taken")
                    return redirect('register')
               elif User.objects.filter(email=email).exists():
                    messages.info(request,"email is taken")
                    return redirect('register')
               else:

                    user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                    user.save();
                    return redirect('login')
          else:
               messages.info(request,"password not matched")
               return redirect('register')

     return render(request, "register.html")
def login(request):
     if request.method == 'POST':
          username=request.POST['username']
          password = request.POST['password']
          user =auth.authenticate(username=username,password=password)

          if user is not None:
               auth.login(request,user)
               return redirect('/')
          else:
              messages.info(request,'invalid')
              return redirect('login')
     return render(request,"login.html")
def logout(request):
     auth.logout(request)
     return redirect('/')
