from rest_framework import status
from rest_framework.generics import GenericAPIView

# 4,二级视图GenericAPIView特点
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from DRFStudy.models import BookInfo
from DRFStudy.views import BookInfoModelSerializer

"""
特点:
1, GenericAPIView,继承自APIView类，为列表视图, 和详情视图,添加了常用的行为和属性。
    行为(方法)
        get_queryset
        get_serializer

    属性
        queryset
        serializer_class

2, 可以和一个或多个mixin类配合使用。
"""


# 5,使用二级视图GenericAPIView实现, 列表视图
class BookListGenericAPIView(GenericAPIView):
    # 1,提供公共的属性
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer
    pagination_class = PageNumberPagination

    def get(self, request):
        books = self.get_queryset()
        page = self.paginate_queryset(books)
        if page is not None:
            # 2,将对象列表转成字典列表
            serializer = self.get_serializer(instance=page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(instance=books, many=True)
        return Response(serializer.data)

    def post(self, request):
        data_dict = request.data
        serializer = self.get_serializer(data=data_dict)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


"""
特点: 
1, GenericAPIView,继承自APIView类，为列表视图, 和详情视图,添加了常用的行为和属性。
    行为(方法)
        get_queryset:  获取queryset的数据集
        get_serializer: 获取serializer_class序列化器对象
        get_object:    根据lookup_field获取单个对象

    属性
        queryset:   通用的数据集
        serializer_class: 通用的序列化器
        lookup_field:   默认是pk,可以手动修改id

2, 可以和一个或多个mixin类配合使用。
"""


# 6,使用二级视图GenericAPIView实现, 详情视图
class BookDetailGenericAPIView(GenericAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer

    def get(self, request, pk):
        book = self.get_object()
        serializer = self.get_serializer(instance=book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        data_dict = request.data
        book = self.get_object()
        serializer = self.get_serializer(instance=book, data=data_dict)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
