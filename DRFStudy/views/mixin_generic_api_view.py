from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin

from DRFStudy.models import BookInfo
from DRFStudy.views import BookInfoModelSerializer

"""
Mixin,特点: 
1, mixin类提供用于提供基本视图行为(列表视图, 详情视图)的操作
2, 配合二级视图GenericAPIView使用的

类名称                 提供方法        功能
ListModelMixin        list          查询所有的数据
CreateModelMixin      create        创建单个对象
RetrieveModelMixin    retrieve      获取单个对象
UpdateModelMixin      update        更新单个对象
DestroyModelMixin     destroy       删除单个对象

"""


class BookListMixinGenericAPIView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class BookDetailMixinGenericAPIView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer
    lookup_url_kwarg = "book_id"

    def get(self, request, book_id):
        return self.retrieve(request)

    def put(self, request, book_id):
        return self.update(request)

    def delete(self, request, book_id):
        return self.destroy(request)
