from django.db import models

# Create your models here.
class Usersinfo(models.Model):
    name=models.CharField(max_length=50,unique=True)
    email=models.EmailField(max_length=50)
    interests=models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name="UserInfo"