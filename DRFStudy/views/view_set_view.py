from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from DRFStudy.models import BookInfo
from DRFStudy.views import BookInfoModelSerializer

"""
视图集
特点:
    1,可以将一组相关的操作, 放在一个类中进行完成
    2,不提供get,post方法, 使用retrieve, create方法来替代
    3,可以将标准的请求方式(get,post,put,delete), 和mixin中的方法做映射

常见的视图集:
类名称                 父类              作用
ViewSet               APIView          可以做路由映射
                      ViewSetMixin

GenericViewSet        GenericAPIView   可以做路由映射,可以使用三个属性,三个方法
                      ViewSetMixin

ModelViewSet          GenericViewSet   所有的增删改查功能,可以使用三个属性,三个方法
                      5个mixin类

ReadOnlyModelViewSet  GenericViewSet   获取单个,所有数据,可以使用三个属性,三个方法
                      RetrieveModelMixin
                      ListModelMixin

"""


class BookViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = BookInfo.objects.all()
        serializer = BookInfoModelSerializer(instance=queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = BookInfo.objects.all()
        book = get_object_or_404(queryset, pk=pk)
        serializer = BookInfoModelSerializer(instance=book)
        return Response(serializer.data)


class BookReadOnlyModelViewSet(ReadOnlyModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer


class BookModelViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer

    # 1,获取阅读量大于20的书籍
    def bread_book(self, request):
        book = self.get_queryset().filter(b_read__gt=20)
        serializer = self.get_serializer(instance=book, many=True)
        return Response(serializer.data)

    # 2,修改书籍编号为1的, 阅读量为99
    def update_partial_book_bread(self, request, pk):
        book = self.get_object()
        data_dict = request.data
        serializer = self.get_serializer(instance=book, data=data_dict, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
