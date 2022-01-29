import random
import time

from django.core.cache import cache
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class HelloMiddle(MiddlewareMixin):

    def process_request(self, request):
        ip = request.META.get("REMOTE_ADDR")
        print(ip)
        if request.path == "/advance/get_phone/":
            if ip == "127.0.0.1":
                if random.randrange(100) > 20:
                    return HttpResponse("恭喜你获得小米8 256G")
        if request.path == "/advance/get_ticket/":
            if ip.startswith("127.0.0"):
                return HttpResponse("已经抢光")
        if request.path == "/advance/search/":
            result = cache.get(ip)
            if result:
                return HttpResponse("您的访问过于频繁，请10s后再次搜索")
            cache.set(ip, ip, timeout=10)

        if request.path == "/advance/hello/":
            # 黑名单、限制请求频率
            black_list = cache.get('black', [])
            if ip in black_list:
                return HttpResponse("黑名单用户")
            requests = cache.get(ip, [])
            while requests and time.time() - requests[-1] > 60:
                requests.pop()
            requests.insert(0, time.time())
            cache.set(ip, requests, timeout=60)
            if len(requests) > 30:
                black_list.append(ip)
                cache.set('black', black_list, timeout=60 * 60 * 24)
                return HttpResponse("小爬虫小黑屋里呆着吧")
            if len(requests) > 10:
                return HttpResponse("请求次数过于频繁，小爬虫回家睡觉吧")
