from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='users.index'),
    path('add-new/', views.Add, name='users.add-user'),
    path('user_delete/<int:id>/', views.Delete, name='user.delete'),
    path('edit/<int:id>/', views.Edit, name='users.edit-user'),

]
