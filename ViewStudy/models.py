from django.db import models


# Create your models here.

class Grade(models.Model):
    g_name = models.CharField(max_length=16, default="", db_index=True, verbose_name="年级名称")

    class Meta:
        verbose_name = "年级"


class Student(models.Model):
    s_name = models.CharField(max_length=16, default="", db_index=True, verbose_name="学生名称")
    s_grade = models.ForeignKey('Grade', null=True, on_delete=models.SET_NULL, related_name="grade")
    s_password = models.CharField(max_length=128, default="", verbose_name="密码")
    s_token = models.CharField(max_length=256, default="", verbose_name="token")

    class Meta:
        verbose_name = "学生"
