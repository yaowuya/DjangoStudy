from django.db import models


# Create your models here.
# 定义图书模型类BookInfo
class BookInfo(models.Model):
    b_title = models.CharField(max_length=20, verbose_name='名称')
    b_pub_date = models.DateField(verbose_name='发布日期')
    b_read = models.IntegerField(default=0, verbose_name='阅读量')
    b_comment = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        verbose_name = '图书'  # 在admin站点中显示的名称

    def data_to_dict(self):
        return {
            "id": self.id,
            "b_title": self.b_title,
            "b_pub_date": self.b_pub_date,
            "b_read": self.b_read,
            "b_comment": self.b_comment,
            "is_delete": self.is_delete,
        }

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.b_title


# 定义英雄模型类HeroInfo
class HeroInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    h_name = models.CharField(max_length=20, verbose_name='名称')
    h_gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    h_comment = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    h_book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')  # 外键
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        verbose_name = '英雄'

    def __str__(self):
        return self.h_name
