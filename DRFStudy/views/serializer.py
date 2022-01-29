"""
定义序列化器:
1, 定义类, 继承自Serializer
2, 编写字段名称, 和模型类一样
3, 编写字段类型, 和模型类一样
4, 编写字段选项, 和模型类一样
    read_only: 只读
    label: 字段说明

序列化器作用:
1, 反序列化: 将json(dict)数据, 转成模型类对象
    ①: 校验
    ②: 入库

2, 序列化: 将模型类对象, 转成json(dict)数据
"""""

from rest_framework import serializers

# 需求: 添加的书籍的日期不能小于2015年
from DRFStudy.models import BookInfo


def check_h_pub_date(date):
    print("date = {}".format(date))
    if date.year < 2015:
        raise serializers.ValidationError("日期不能小于2015年")
    return date


# 1,定义书籍序列化器
class BookInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, label="书籍编号")
    b_title = serializers.CharField(max_length=20, label="名称")
    b_pub_date = serializers.DateField(validators=[check_h_pub_date], label="发布日期")
    b_read = serializers.IntegerField(default=0, min_value=0, label="阅读量")
    b_comment = serializers.IntegerField(default=0, max_value=50, label="评论量")
    is_delete = serializers.BooleanField(default=False, label="逻辑删除")

    # 1,关联英雄字段, 在一方中,输出多方内容的时候加上many=True
    # heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    heroinfo_set = serializers.StringRelatedField(read_only=True, many=True)

    # 3, 单字段校验, 方法; 需求: 添加的书籍必须包含'金瓶'
    def validate_b_title(self, value):
        print("value = {}".format(value))
        # 1,判断传入的value中是否包含金瓶
        if "金瓶" not in value:
            raise serializers.ValidationError("书名必须包含金瓶")
        return value

    # 4,多字段校验, 方法; 添加书籍的时候,评论量不能大于阅读量
    def validate(self, attrs):
        """
       :param attrs: 外界传入的需要校验的字典
       :return:
       """
        print("value = {}".format(attrs))
        # 1,判断评论量和阅读量的关系
        if attrs["b_read"] < attrs["b_comment"]:
            raise serializers.ValidationError("评论量不能大于阅读量")
        return attrs

    # 5,重写create方法,实现数据入库
    def create(self, validated_data):
        print("validated_data = {}".format(validated_data))
        book = BookInfo.objects.create(**validated_data)
        return book

    def update(self, instance, validated_data):
        """
        :param instance: 需要更新的对象
        :param validated_data: 验证成功之后的数据
        :return:
        """
        # 1,更新数据
        instance.b_title = validated_data["b_title"]
        instance.b_pub_date = validated_data["b_pub_date"]
        instance.b_read = validated_data["b_read"]
        instance.b_comment = validated_data["b_comment"]
        instance.save()

        book = BookInfo.objects.get(id=instance.id)
        return book


# 2,定义英雄序列化器
class HeroInfoSerializer(serializers.Serializer):
    """英雄数据序列化器"""
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    id = serializers.IntegerField(read_only=True, label="ID")
    h_name = serializers.CharField(max_length=20, label="名字")
    h_gender = serializers.ChoiceField(choices=GENDER_CHOICES, required=False, label="性别")
    h_comment = serializers.CharField(max_length=20, required=False, allow_null=True, label="描述信息")
    # 1,添加外键,主键表示 必须提供`queryset` 选项, 或者设置 read_only=`True`.
    # h_book = serializers.PrimaryKeyRelatedField(queryset=BookInfo.objects.all())
    # h_book = serializers.PrimaryKeyRelatedField(read_only=True)

    # 2,添加外键, 来自于关联模型类, __str__的返回值
    # h_book = serializers.StringRelatedField(read_only=True)

    # 3,添加外键,关联另外一个序列化器
    h_book = BookInfoSerializer(read_only=True)


class BookInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo  # 参考模型类生成字段
        fields = "__all__"  # 生成所有字段
        # 2,设置只读字段
        # read_only_fields = ["b_title", "b_pub_date"]
        # 3,给生成的字段添加额外约束
        extra_kwargs = {
            "b_read": {
                "max_value": 999999,
                "min_value": 0
            },
            "b_comment": {
                "max_value": 888888,
                "min_value": 0
            }
        }
