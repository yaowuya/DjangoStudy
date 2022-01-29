from django.db import models


# Create your models here.

class UserModel(models.Model):
    username = models.CharField(max_length=16, unique=True, verbose_name="用户名")
    icon = models.ImageField(upload_to="icons")

    class Meta:
        verbose_name = "用户"
