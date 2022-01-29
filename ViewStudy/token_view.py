import hashlib
import time

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from ViewStudy.models import Student


def register(request):
    if request.method == "GET":
        return render(request, "studentRegister.html")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(request.body)
        try:
            student = Student()
            student.s_name = username
            student.s_password = password
            student.save()
        except Exception as e:
            print(str(e))
            return redirect(reverse("view:register"))
        return redirect(reverse("view:student_login"))


def student_login(request):
    if request.method == "GET":
        return render(request, "studentLogin.html")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(request.body)
        students = Student.objects.filter(s_name=username, s_password=password)
        if students.exists():
            student = students.first()
            ip = request.META.get("REMOTE_ADDR")
            token = generate_token(ip, username)
            student.s_token = token
            student.save()
            response = HttpResponse("注册成功")
            response.set_cookie("token", token)
            return response
        return redirect(reverse("view:register"))


def generate_token(ip, username):
    c_time = time.ctime()
    r = username
    return hashlib.new("md5", (ip + c_time + r).encode("utf-8")).hexdigest()


def student_mine(request):
    token = request.COOKIES.get("token")
    try:
        student = Student.objects.get(s_token=token)
    except Exception as e:
        print(str(e))
        return redirect(reverse("view:student_login"))
    return HttpResponse(student.s_token)
