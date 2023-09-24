from django.shortcuts import render
from app1.models import Place,Team,Myuser
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def home(request):
    p=Place.objects.all()
    t=Team.objects.all()
    return render(request,'home.html',{'p':p,'t':t})
def sign_up(request):
        if (request.method == "POST"):
            u= request.POST['u']
            f= request.POST['f']
            l= request.POST['l']
            e= request.POST['e']
            p= request.POST['p']
            pl=request.POST['pl']
            ph=request.POST['ph']
            b=Myuser.objects.create_user(username=u,first_name=f,last_name=l,email=e,password=p,place=pl,phone=ph)
            b.save()
            return home(request)
        return render(request,'signup.html')
def user_login(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p= request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return home(request)
        else:
            messages.error(request,"invalid credentials")
    return render(request,'login.html')
@login_required
def user_logout(request):
    logout(request)
    return user_login(request)