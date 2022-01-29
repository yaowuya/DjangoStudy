from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

# 10,三级视图,实现列表,详情视图
from DRFStudy.models import BookInfo
from DRFStudy.views import BookInfoModelSerializer


class BookListThirdView(ListAPIView, CreateAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer


class BookDetailThirdView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer
