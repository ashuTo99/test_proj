
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render
from movies.models import Movies,UserMovies
from users.models import CustomUser
from .forms import MoviesAddForm,moviesForm,AssignMoviesForm
from test_proj.service import mqttService

@login_required(login_url='login')
def index(request):
    movies = Movies.objects.filter(is_active = True)
    content = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', content)



@login_required(login_url='login')
def Delete(request, id):
    if not request.user.is_superuser:
        return redirect('movies.index')
    movie = Movies.objects.get(id=id)
    if not movie:
        return redirect('movies.index')
    movie.delete()
    mqttService('movie delete successfully')
    return redirect('movies.index')


@login_required(login_url='login')
def Edit(request, id):
    if not request.user.is_superuser:
        return redirect('movies.index')
    movie = Movies.objects.get(id=id)
    if not movie:
        return redirect('movies.index')
    initial_dict = {
        "name": movie.name,
        "poster": movie.poster,
    }
    form = moviesForm(initial=initial_dict)
    if request.method == "POST":
        form = moviesForm(request.POST,request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            mqttService('movie edit successfully')

            return redirect('movies.index')

    context = {
        'form': form,
        'movie': movie,
    }
    return render(request, 'movies/edit.html', context)


@login_required(login_url='login')
def Add(request):
    if not request.user.is_superuser:
        return redirect('movies.index')
    if request.method == 'POST':
        form = MoviesAddForm(request.POST,request.FILES)
        if form.is_valid():
            movie = Movies()
            movie.name = form.cleaned_data.get('name')
            movie.poster = form.cleaned_data.get('poster')
            movie.save()
            mqttService('movie added successfully')

            return redirect('movies.index')
    else:
        form = MoviesAddForm()
    context = {
        "form": form,

    }
    return render(request, "movies/add.html", context)

@login_required(login_url='login')
def AssignMovies(request):
    if not request.user.is_superuser:
        return redirect('movies.index')
    if request.method == 'POST':
        form = AssignMoviesForm(request.POST)
        if form.is_valid():
            users = form.cleaned_data.get('users')
            posters = form.cleaned_data.get('posters')
            for post in posters:
                for user in users:
                    assignPoster = UserMovies()
                    assignPoster.user = user
                    assignPoster.poster = post
                    assignPoster.save()
            mqttService('posters assigned to users')
            return redirect('movies.index')
    else:
        form = AssignMoviesForm()
    context = {
        "form": form,

    }
    return render(request, "movies/assign_movies.html", context)
    
@login_required(login_url='login')
def showPosters(request):
    posters = UserMovies.objects.filter(user = request.user)
    content = {
        'posters': posters,
    }
    return render(request, 'movies/posters.html', content)



