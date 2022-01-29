import os

from django.http import HttpResponse
from django.shortcuts import render


from DjangoStudy.settings import MEDIA_ROOT
from FileStudy.models import UserModel


def hello_world(request):
    return HttpResponse("hello world ...")


def index(request):
    username = "admin"
    return render(request, "file/index.html", context=locals())


def upload_file(request):
    if request.method == "GET":
        return render(request, "file/upload.html")
    if request.method == "POST":
        icon = request.FILES.get("icon")
        print(icon)
        with open(os.path.join(MEDIA_ROOT, "icon.jpg"), 'wb') as save_file:
            for part in icon.chunks():
                save_file.write(part)
                save_file.flush()
        return HttpResponse("上传成功")


def image_upload(request):
    if request.method == "GET":
        return render(request, "file/imageUpload.html")
    if request.method == "POST":
        username = request.POST.get("username")
        icon = request.FILES.get("icon")
        user = UserModel()
        user.username = username
        user.icon = icon
        user.save()
        return HttpResponse("上传成功," + username)


def mine(request):
    username = request.GET.get("username")
    user = UserModel.objects.get(username=username)
    print("/static/upload/" + user.icon.url)
    data = {
        "username": username,
        "icon_url": "/static/upload/" + user.icon.url
    }
    return render(request, "file/mine.html", context=data)
