from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from DRFStudy.models import BookInfo
from DRFStudy.packages.pagination import MyPageNumberPagination
from DRFStudy.views import BookInfoModelSerializer


class BookInfoModelViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer
    pagination_class = MyPageNumberPagination

    # 1,获取阅读量大于20的书籍
    @action(methods=["GET"], detail=False)
    def bread_book(self, request):
        book = self.get_queryset().filter(b_read__gt=20)
        serializer = self.get_serializer(instance=book, many=True)
        return Response(serializer.data)

    # 2,修改书籍编号为1的, 阅读量为99
    @action(methods=["PUT"], detail=True)
    def update_partial_book_bread(self, request, pk):
        book = self.get_object()
        data_dict = request.data
        serializer = self.get_serializer(instance=book, data=data_dict, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
