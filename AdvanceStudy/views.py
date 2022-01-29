from time import sleep

from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page


# 数据库缓存
@cache_page(30)
def news(request):
    news_list = []
    for i in range(10):
        news_list.append("最近贸易战又开始了%d" % i)

    sleep(5)
    data = {
        "news_list": news_list
    }
    return render(request, 'advance/news.html', context=data)


def redis_news(request):
    result = cache.get("news")
    if result:
        return HttpResponse(result)
    news_list = []
    for i in range(10):
        news_list.append("最近贸易战又开始了%d" % i)

    sleep(5)
    data = {
        "news_list": news_list
    }
    response = render(request, 'advance/news.html', context=data)
    cache.set("news", response.content, timeout=60)
    return response
