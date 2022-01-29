from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from RestStudy.models import Book


@csrf_exempt
def books(request):
    if request.method == "GET":
        book_list = Book.objects.all()
        book_list_json = []
        for book in book_list:
            book_list_json.append(book.to_dict())
        data = {
            "status": 200,
            "msg": "ok",
            "data": book_list_json
        }
        return JsonResponse(data=data)
    if request.method == "POST":
        params = request.POST
        b_name = params.get("b_name")
        b_price = params.get("b_price", 1)

        book = Book()
        book.b_name = b_name
        book.b_price = b_price
        book.save()

        data = {
            "status": 201,
            "msg": "add success",
            "data": book.to_dict()
        }
        return JsonResponse(data=data)


@csrf_exempt
def book(request, book_id):
    book_obj = Book.objects.get(id=book_id)
    if request.method == "GET":
        data = {
            "status": 200,
            "msg": "ok",
            "data": book_obj.to_dict()
        }
        return JsonResponse(data=data)

    if request.method == "PATCH":
        param = request.GET
        b_name = param.get("b_name")
        b_price = param.get("b_price", 1)
        book_obj.b_name = b_name
        book_obj.b_price = b_price
        book_obj.save()
        data = {
            "status": 200,
            "msg": "ok",
            "data": book_obj.to_dict()
        }
        return JsonResponse(data=data)
    if request.method == "DELETE":
        book_obj.delete()
        data = {
            "status": 204,
            "msg": "delete success",
            "data": {}
        }
        return JsonResponse(data=data)
