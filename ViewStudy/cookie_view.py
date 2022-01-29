from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse


def set_cookie(request):
    response = HttpResponse("设置cookie")
    username = "小明"
    # 支持中文的做法
    response.set_cookie("username", username.encode('utf-8').decode('latin-1'))
    return response


def get_cookie(request):
    username = request.COOKIES.get("username")
    return HttpResponse(username.encode('latin-1').decode('utf-8'))


def login(request):
    return render(request, "login.html")


def do_login(request):
    uname = request.POST.get('uname')
    response = HttpResponseRedirect(reverse("view:mine"))
    # response.set_cookie('uname', uname, max_age=60)
    response.set_signed_cookie('uname', uname, 'study', max_age=10)
    return response


def mine(request):
    # uname = request.COOKIES.get("uname")
    try:
        uname = request.get_signed_cookie('uname', salt='study')
        if uname:
            return render(request, 'mine.html', context={"uname": uname})
        return redirect(reverse("view:login"))
    except Exception as e:
        print(e)
        return redirect(reverse("view:login"))


def logout(request):
    response = redirect(reverse("view:login"))
    response.delete_cookie('uname')
    return response
