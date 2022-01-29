from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# 2,序列化器和APIView实现列表视图
from DRFStudy.models import BookInfo
from DRFStudy.views.serializer import BookInfoModelSerializer


class BookListAPIView(APIView):
    def get(self, request):
        books = BookInfo.objects.all()
        serializer = BookInfoModelSerializer(instance=books, many=True)
        return Response(serializer.data)

    def post(self, request):
        data_dict = request.data
        serializer = BookInfoModelSerializer(data=data_dict)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 3,序列化器和APIView实现详情视图
class BookDetailAPIView(APIView):
    def get(self, request, book_id):
        book = BookInfo.objects.get(id=book_id)
        serializer = BookInfoModelSerializer(instance=book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, book_id):
        data_dict = request.data
        book = BookInfo.objects.get(id=book_id)
        serializer = BookInfoModelSerializer(instance=book, data=data_dict)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, book_id):
        BookInfo.objects.get(id=book_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
