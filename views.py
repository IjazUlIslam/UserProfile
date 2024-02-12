from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm
from .forms import LoginForm
from .forms import EditProfile
from .forms import EditPassword
from django.contrib import messages
from django.contrib.auth import logout
from UserProfile.models import CustomUser
import os


# Signup View function
def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST, request.FILES)
        if fm.is_valid():

            # Retrieving data from FORM
            first_name = fm.cleaned_data['first_name']
            last_name = fm.cleaned_data['last_name']
            email = fm.cleaned_data['email']
            phone_number = fm.cleaned_data['phone_number']
            password = fm.cleaned_data['password']
            password_confirm = fm.cleaned_data['password_confirm']
            upload_image = fm.cleaned_data['upload_image']

            # Password Validation
            if password != password_confirm:
                messages.error(request, "The password do not match")

            # Save in models
            b = CustomUser(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                password=password,
                upload_image=upload_image
            )
            b.save()

            # success message throw
            messages.success(request, 'Account Created Successfully')

            return HttpResponseRedirect('/login')
    else:
        fm = SignUpForm()
    return render(request, 'UserProfile/signup.html', {'form': fm})


# Login View function
def user_login(request):
    fm = LoginForm()
    return render(request, 'UserProfile/userlogin.html', {'form': fm})


# Profile function
def user_profile(request):
    if request.method == "POST":
        fm = EditProfile(request.POST, request.FILES)
        if fm.is_valid():
            first_name = fm.cleaned_data['first_name']
            last_name = fm.cleaned_data['last_name']
            phone_number = fm.cleaned_data['phone_number']
            email = fm.cleaned_data['email']
            new_upload_image = fm.cleaned_data['upload_image']
            user = CustomUser.objects.get(email=request.user.email)
            user.first_name = first_name
            user.last_name = last_name
            user.phone_number = phone_number
            user.email = email
            old_upload_image = user.upload_image
            if new_upload_image != old_upload_image:
                os.remove(old_upload_image.path)
                user.upload_image = new_upload_image
            user.save()
            messages.success(request, 'Profile Updated !')
            upload_image = user.upload_image.url
    else:
        user = CustomUser.objects.get(email=request.user.email)
        data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'phone_number': user.phone_number,
            'full_name': user.full_name,
            'login_date': user.login_date
        }
        fm = EditProfile(initial=data)
        upload_image = user.upload_image.url
    return render(
        request,
        'UserProfile/profile.html',
        {'name': request.user, 'form': fm, 'upload_image': upload_image}
    )


# Logout function
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    else:
        messages.success(request, 'user not login yet')
    return HttpResponseRedirect('/login')


# change password
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = EditPassword(data=request.POST)
            if fm.is_valid():
                password = fm.cleaned_data['new_password']
                # update password
                user = CustomUser.objects.get(email=request.user.email)
                user.password = password
                user.save()
                return HttpResponseRedirect('/profile/')
        else:
            fm = EditPassword()
    else:
        messages.error(request, "You need to login, to change password")
        return HttpResponseRedirect('/login/')
    return render(request, 'UserProfile/changepass.html', {'form': fm})
