from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='movies.index'),
    path('add/', views.Add, name='movie.add'),
    path('delete/<int:id>/', views.Delete, name='movie.delete'),
    path('edit/<int:id>/', views.Edit, name='movie.edit'),
    path('assign-movies/', views.AssignMovies, name='movie.assign'),
    path('dashboard/', views.showPosters, name='posters.dashboard'),



]
