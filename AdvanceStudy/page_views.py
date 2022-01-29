from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from AdvanceStudy.models import Animal


def add_animals(request):
    result = []
    for i in range(10000):
        result.append(Animal(
            name="小猫%d" % i,
            age=i
        ))
    Animal.objects.bulk_create(result)
    return HttpResponse("创建成功")


def get_animals(request):
    params = request.GET
    page = int(params.get("page", 1))
    page_size = int(params.get("page_size", 10))
    animals = Animal.objects.all()
    paginator = Paginator(animals, page_size)
    page_object = paginator.page(page)
    print(paginator.count, page_object.number)
    data = {
        "page_list": page_object.object_list,
        "page_range": paginator.page_range
    }
    return render(request, "advance/animals.html", context=data)
