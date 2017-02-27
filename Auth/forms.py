from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from Auth.models import TechProfile, College, year_choices

class RegisterForm(forms.ModelForm):
    name = forms.CharField(label="Name",
                               widget=forms.TextInput(attrs={'class': 'form-control','required':'true','placeholder':'First Name',}))
    email = forms.EmailField(label="Email",widget=forms.TextInput(attrs={'class':'form-control','required':'true','placeholder':'Email'}))

    password = forms.CharField(label="Password",
                               widget=forms.TextInput(attrs={'class': 'form-control','required':'true','type':'password', 'placeholder':'Password', 'name': 'password'}))

    year = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control', 'required':'true', }),choices=year_choices,)

   # college = forms.ModelChoiceField(queryset = College.objects.all() ,widget=forms.Select(attrs={'class': 'form-control'}))

    mobileNumber = forms.IntegerField(label="Mobile Number",
                               widget=forms.TextInput(attrs={'class': 'form-control','type':'number', 'required':'true','placeholder':"Mobile Number"}))


    class Meta:
        model = TechProfile
        fields = ['first_name', 'last_name','email','password','year','college','mobile_number']
        exclude = ['user_id','user','profile_photo','college']

'''
class FbForm(forms.ModelForm):

    year = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control', 'required':'true','placeholder':'Year', }),choices=year_choices,)

    college = forms.CharField(label="College",
                               widget=forms.TextInput(attrs={'class': 'form-control','type':'text','required':'true', 'placeholder':"College"}))

    mobile_number = forms.IntegerField(label="Mobile Number",
                               widget=forms.TextInput(attrs={'class': 'form-control','type':'number', 'required':'true','placeholder':"Mobile Number"}))


    class Meta:
        model = TechProfile
        fields = ['year','college','mobile_number']
        exclude = ['user_id','user','profile_photo']


class Tech2CAForm(forms.ModelForm):
    whatsapp_number = forms.IntegerField(label="WhatsApp Number",
                               widget=forms.TextInput(attrs={'class': 'form-control','type':'text', 'placeholder':"WhatsApp Number"}))

    college_address = forms.CharField(label="College Address",
                               widget=forms.Textarea(attrs={'class': 'form-control','type':'textarea', 'rows': '5','placeholder':"College Address"}))

    postal_address = forms.CharField(label="Postal Address",
                               widget=forms.Textarea(attrs={'class': 'form-control','type':'textarea','rows': '5', 'placeholder':"Postal Address"}))

    pincode = forms.IntegerField(label="Pincode",
                               widget=forms.TextInput(attrs={'class': 'form-control','type':'number', 'placeholder':"Pincode"}))


    class Meta:
        model = CAProfile
        fields = ['whatsapp_number','college_address','postal_address','pincode',]


'''

class LoginForm(forms.Form):
    email = forms.CharField(label="email",
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Email','required':'true', 'type':'text','name': 'email'}))
    password = forms.CharField(label="Password",
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Password','required':'true', 'type':'password','name': 'password'}))
