# Generated by Django 3.2.11 on 2022-01-19 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=16)),
                ('icon', models.ImageField(upload_to='icons')),
            ],
            options={
                'verbose_name': '用户',
            },
        ),
    ]
