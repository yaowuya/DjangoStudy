import random

from django.http import HttpResponse


def get_phone(request):
    if random.randrange(100) > 95:
        return HttpResponse("恭喜你抢到小米8")
    return HttpResponse("正在排队....")


def get_ticket(request):
    return HttpResponse("还剩余99张满100-99")


def search(request):
    return HttpResponse("这是你搜索到的种子资源")


def hello(request):
    return HttpResponse("hello")
