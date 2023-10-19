from django.shortcuts import render, redirect
from userauth.forms import UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def register_view(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST or None)

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


def login_view():
    return None


def logout_view():
    return None