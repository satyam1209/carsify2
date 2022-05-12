from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import Group,User
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
def index(request):
    return render(request,"car/base.html")

# Login
def user_login(request):
	# to check if user is authnticated or not if not then it will enter if condition
	if not request.user.is_authenticated:
		# to check weather the request is post or get
		if request.method=="POST":
			# collected login credentials from form
			form= LoginForm(request=request,data=request.POST)
			# checking if the form is filed correctly or not
			if form.is_valid():
				# accessing name and password for authentication
				uname=form.cleaned_data['mail']
				upass=form.cleaned_data['password']
				# here authenticating usuing given login credentials
				user=authenticate(Email=uname,password=upass)
				# if a valid user is found
				if user is not None:
                # login is initiated here
					login(request,user)
					# message for successfull login
					messages.success(request,"Login Successfull !!!")
					# redirecting to index page afer login 
					return HttpResponseRedirect('/')
		else:
			# if get request id passed we took the html for forn
			form=LoginForm()
			# rendered for html page
		return render(request,'login.html',{'form':form})
	else:
		print("b")
		return HttpResponseRedirect('/')

# signup
def signup(request):
	# if request id post
	if request.method=='POST':
		# collecting data
		form=SignUpForm(request.POST)
		# if filled form is valid
		if form.is_valid():
			# if yes put a message for successful signup
			messages.success(request,"Congratulation!! you have become an Member")
			# save the credenials
			form.save()
	else:
		# in case of get request
		form=SignUpForm()
		# render the bodey of the form
	return render(request,'car/signup.html',{'form':form})


# Create your views here.
