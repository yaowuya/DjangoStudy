from django.db import models


# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=100, default="", verbose_name="名称", db_index=True)
    age = models.IntegerField(default=0, verbose_name="年龄")

    class Meta:
        verbose_name = "动物"
