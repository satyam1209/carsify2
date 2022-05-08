from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import Group,User
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
def index(request):
    return render(request,"car/base.html")

# Login
def user_login(request):
	if not request.user.is_authenticated:
		if request.method=="POST":
			form= LoginForm(request=request,data=request.POST)
			if form.is_valid():
				uname=form.cleaned_data['username']
				upass=form.cleaned_data['password']
				user=authenticate(username=uname,password=upass)
				if user is not None:
					login(request,user)
					messages.success(request,"Login Successfull !!!")
					return HttpResponseRedirect('/')
		else:
			form=LoginForm()
		return render(request,'car/login.html',{'form':form})
	else:
		return HttpResponseRedirect('/')

# signup
def signup(request):
	if request.method=='POST':
		form=SignUpForm(request.POST)
		if form.is_valid():
			messages.success(request,"Congratulation!! you have become an Member")
			form.save()
			# group = Group.objects.get(name="Author")
			# user.groups.add(group)
	else:
		form=SignUpForm()
	return render(request,'car/signup.html',{'form':form})


# Create your views here.
