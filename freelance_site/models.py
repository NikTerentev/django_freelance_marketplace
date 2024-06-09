from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Performer(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=11)
    email = models.CharField(max_length=50)
    experience = models.TextField()
    profile_pic = models.ImageField(upload_to='profiles/', blank=True)

    def __str__(self):
        return f"{self.id} | {self.name}"


class Customer(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=11)
    email = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='profiles/', blank=True)

    def __str__(self):
        return f"{self.id} | {self.name}"
