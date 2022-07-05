from django.contrib.auth.models import User
from django.db import models

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=50)
    sana = models.DateTimeField(auto_now_add=True)
    mavzu = models.CharField(max_length=100)
    matn = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        self.sarlavha
