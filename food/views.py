import profile
from sre_constants import SUCCESS
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import UserSignUp,EditAdminForm,EditUserForm,UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.
def home(request):
  return render (request,'food/index.html')

def user_signup(request):
  if request.method == 'POST':
    form = UserSignUp(request.POST)
    if form.is_valid():
      form.save()
      messages.SUCCESS(
                request, 'Your account has been created successfully')
      return HttpResponseRedirect('/login/')

  else:
    form = UserSignUp()
  return render(request,'food/signup.html',{'form':form})



def user_login(request):
    if not request.user.is_authenticated:
      if request.method == 'POST':
          fm = UserLoginForm(request=request, data=request.POST)
          if fm.is_valid():
              uname = fm.cleaned_data['username']
              upass = fm.cleaned_data['password']
              user = authenticate(username=uname, password=upass)
              if user is not None:
                  login(request, user)
                  messages.SUCCESS(request, 'Login successfully')
                  return HttpResponseRedirect('/profile/')
          else:
            return HttpResponse("something wrong")
      else:
          fm = UserLoginForm()
          return render(request, 'food/login.html', {'form': fm})
    else:
        return HttpResponseRedirect('/profile/')





def user_profile(request):
    if request.user.is_authenticated:
        return render (request,'food/profile.html',{'name':request.user.username})
        # if request.method == 'POST':
        #     if request.user.is_superuser == True:
        #         fm = EditAdminForm(request.POST, instance=request.user)
        #         users = User.objects.all()
        #     else:
        #         fm = EditUserForm(request.POST, instance=request.user)
        #         users = None
        #     if fm.is_valid():
        #         messages.success(request, 'data update successfully !!')
        #         fm.save()
        # else:
        #     if request.user.is_superuser == True:
        #         fm = EditAdminForm(instance=request.user)
        #         users = User.objects.all()
        #     else:
        #         fm = EditUserForm(instance=request.user)
        #         users = None
        # return render(request, 'home/profile.html', {'name': request.user, 'form': fm, 'users': users})
    else:
        return HttpResponseRedirect('/login/')

def user_Logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

