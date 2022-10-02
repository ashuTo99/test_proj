from email.policy import default
from statistics import mode
from django.db import models
from users.models import CustomUser

class Movies(models.Model):
    name = models.CharField(max_length=250)
    poster = models.ImageField(upload_to='uploads/movies')
    is_active = models.BooleanField(default = True)
    created_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name
    

class UserMovies(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    poster = models.ForeignKey(Movies,on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.user.name)

