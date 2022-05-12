from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _


class SignUpForm(UserCreationForm):
	password1= forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password2= forms.CharField(label='Password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
	class Meta:
		model = User
		fields=['username','first_name','last_name','email']
		label={'first_name':'FirstName','last_name':'LastName','email':'Email'}
		widgets ={'username': forms.TextInput(attrs={'class':'form-control'}),
		'first_name': forms.TextInput(attrs={'class':'form-control','required':True,}),
		'last_name': forms.TextInput(attrs={'class':'form-control','required':True,}),
		'email': forms.EmailInput(attrs={'class':'form-control','required':True,}),
		}

class LoginForm(AuthenticationForm):
	username=UsernameField(label='UserName',widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
	password=forms.CharField(label=_('Pasword'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
