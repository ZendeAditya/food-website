
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm
# Modify User signup form
class UserSignUp(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter passowrd'}))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter passowrd (again)'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-label form-control form-text', 'placeholder': 'Enter UserName Here'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-label form-control', 'placeholder': 'Enter Name Here'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-label form-control', 'placeholder': 'Enter Last Name Here'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-label form-control', 'placeholder': 'Enter Email Here'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-label form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-label form-control'






class UserLoginForm(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-label form-control form-text',
        'placeholder':'password'
    }))
    class Meta:
        model = User
        fields = ['username','password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-label form-control form-text', 'placeholder': 'Enter UserName Here'
            }),
        }
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-label form-control'
        self.fields['password'].widget.attrs['class'] = 'form-label form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter username Here'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter password Here'



class EditUserForm(UserChangeForm):
  password=None
  class Meta:
    model = User
    fields = {'username','first_name','last_name','email','date_joined','last_login'}


class EditAdminForm(UserChangeForm):
  password=None
  class Meta:
    model = User
    fields = '__all__'