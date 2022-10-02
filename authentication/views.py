from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.core.mail import BadHeaderError
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
from .forms import LoginForm
from django.contrib.auth.hashers import make_password

@csrf_exempt
def login(request):
    if request.user.is_authenticated:
        return redirect('users.index')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request,email=email, password=password)
            if user is not None:
                auth_login(request, user)
                if request.user.is_superuser:
                    return redirect("users.index")
                else:
                    return redirect("posters.dashboard")
                
            else:
                messages.error(request, 'invalid credentials')
                return redirect("login")
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = LoginForm()
    context = {
        "form": form
    }
    return render(request, "accounts/login.html",context)

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect("login")

