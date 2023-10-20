from django.shortcuts import render, redirect
from userauth.forms import UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from userauth.models import User

# Create your views here.
def register_view(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
            )
            login(request, new_user)
            return redirect('core:index')
        else:
            for field, errors in form.errors.items():
                messages.error(request, f"Field '{field}': {', '.join(errors)}")

    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'userauth/sign-up.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('core:index')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except Exception as e:
            messages.error(request, 'User does not exist')


        user = authenticate(
            username=email,
            password=password
        )

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.first_name}!")
            return redirect('core:index')
        else:
            messages.error(request, 'Email or password is incorrect')

    return render(request, 'userauth/login.html', {})


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('userauth:login')