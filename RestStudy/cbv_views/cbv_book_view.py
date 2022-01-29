from django.http import JsonResponse
from django.views import View

from RestStudy.models import Book


class BooksCBV(View):
    """class base view"""

    def get(self, request):
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

    def post(self, request):
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
