from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse


def session_login(request):
    if request.method == "GET":
        return render(request, "sessionLogin.html")
    if request.method == "POST":
        username = request.POST.get("username")
        request.session['username'] = username
        return redirect(reverse("view:session_mine"))


def session_mine(request):
    username = request.session.get("username")
    return render(request, "sessionMine.html", context=locals())


def session_logout(request):
    response = redirect(reverse("view:session_login"))
    # del request.session['username']
    # response.delete_cookie("sessionid")
    # session cookie 一起清除
    request.session.flush()
    return response
