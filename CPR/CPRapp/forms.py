from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from CPRapp.models import ImProfile

class UsForm(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"password"}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"confirm password"}))
	class Meta:
		model=User
		fields=['username','email',]
		widgets={
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Username",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control",
			"placeholder":"Email",
			}),
		}
class ImForm(forms.ModelForm):
	class Meta:
		model = ImProfile
		fields = ["age","gender","contactno","aadharno","doorno"]
		widgets = {
		"age":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Update Your Age",
			}),
		"gender":forms.Select(attrs={
			"class":"form-control",
			"placeholder":"Select Your Gender",
			}),
		"contactno":forms.TextInput(attrs={
			"class":"form-control","placeholder":"Enter Your Contact no",
			}),
		"aadharno":forms.TextInput(attrs={
			"class":"form-control","placeholder":"Enter your Aadhar no",
			}),
		"doorno":forms.TextInput(attrs={
			"class":"form-control","placeholder":"Enter your door-no",
			}),
		}
class UtupForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","email"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control",
			"placeholder":"Update Emailid",
			}),
		}