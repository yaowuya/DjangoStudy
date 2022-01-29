from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from DRFStudy.models import BookInfo


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = "__all__"


class BookViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookSerializer
