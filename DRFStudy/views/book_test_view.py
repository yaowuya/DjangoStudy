import json
from datetime import datetime

from django.http import JsonResponse, HttpResponse
from django.views import View

from DRFStudy.models import BookInfo


class BooksAPIVIew(View):
    """
    查询所有图书、增加图书
    """

    def get(self, request):
        """
        查询所有图书
        路由：GET /books/
        """
        queryset = BookInfo.objects.all()
        book_list = []
        for book in queryset:
            book_list.append({
                'id': book.id,
                'b_title': book.b_title,
                'b_pub_date': book.b_pub_date,
                'b_read': book.b_read,
                'b_comment': book.b_comment
            })
        return JsonResponse(book_list, safe=False)

    def post(self, request):
        """
        新增图书
        路由：POST /books/
        """
        book_dict = json.loads(request.body)

        # 此处详细的校验参数省略

        book = BookInfo.objects.create(
            b_title=book_dict.get('b_title'),
            b_pub_date=datetime.strptime(book_dict.get('b_pub_date'), '%Y-%m-%d').date()
        )

        return JsonResponse(book.data_to_dict(), status=201)


class BookAPIView(View):
    def get(self, request, pk):
        """
        获取单个图书信息
        路由： GET  /books/<pk>/
        """
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        return JsonResponse(book.data_to_dict())

    def put(self, request, pk):
        """
        修改图书信息
        路由： PUT  /books/<pk>
        """
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        book_dict = json.loads(request.body)

        # 此处详细的校验参数省略

        book.b_title = book_dict.get('b_title')
        book.b_pub_date = datetime.strptime(book_dict.get('b_pub_date'), '%Y-%m-%d').date()
        book.save()

        return JsonResponse(book.data_to_dict())

    def delete(self, request, pk):
        """
        删除图书
        路由： DELETE /books/<pk>/
        """
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        book.delete()

        return HttpResponse(status=204)

