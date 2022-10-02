
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render
from users.models import CustomUser
from .forms import UserAddForm, userForm
from test_proj.service import mqttService


@login_required(login_url='login')
def index(request):
    if request.user.is_superuser:
        users = CustomUser.objects.filter(is_deleted=0,is_superuser = False)
        content = {
            'users': users,
        }
        return render(request, 'users/index.html', content)
    return redirect('movies.index')



@login_required(login_url='login')
def Delete(request, id):
    if request.user.is_superuser:
        user = CustomUser.objects.get(id=id)
        if not user:
            return redirect('users.index')

        user.email = user.email + '_deleted_' + str(id)
        user.is_deleted = True
        user.is_active = False
        user.save()
        mqttService('user delete success')

        return redirect('users.index')
    return redirect('movies.index')


@login_required(login_url='login')
def Edit(request, id):
    if not request.user.is_superuser:
        return redirect('movies.index')

    UserDetail = CustomUser.objects.get(id=id)
    if not UserDetail:
        return redirect('users.index')
    initial_dict = {
        "email": UserDetail.email,
        "name": UserDetail.name,
    }
    form = userForm(initial=initial_dict)
    if request.method == "POST":
        form = userForm(request.POST, instance=UserDetail)
        if form.is_valid():
            form.save()
            mqttService('user edit success')

            return redirect('users.index')

    context = {
        'form': form,
        'user_data': UserDetail,
    }
    return render(request, 'users/edit.html', context)



@login_required(login_url='login')
def Add(request):
    if not request.user.is_superuser:
        return redirect('movies.index')
    if request.method == 'POST':
        form = UserAddForm(request.POST)
        if form.is_valid():
            users = CustomUser()
            users.name = form.cleaned_data["name"]
            users.email = form.cleaned_data["email"]
            users.password = make_password(form.cleaned_data["password"])
            users.confirm_password = make_password(form.cleaned_data["confirm_password"])
            users.save()
            mqttService('user added success')

            return redirect('users.index')
    else:
        form = UserAddForm()
    context = {
        "form": form,

    }
    return render(request, "users/add.html", context)


