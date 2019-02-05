from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have logged in successfully")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form' : login_form})

@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "You have been logged out successfully")
    return redirect(reverse('index'))

def registration(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
   
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'], password = request.POST['password1'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have registered successfully")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register your details at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {'registration_form' : registration_form})

@login_required
def user_profile(request):
    user = User.objects.get(email=request.user.email)
    print(user.pk)
    return render(request, 'profile.html',{'profile':user})