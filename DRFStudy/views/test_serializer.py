from DRFStudy.models import BookInfo, HeroInfo
from DRFStudy.views.serializer import BookInfoSerializer, HeroInfoSerializer, BookInfoModelSerializer

"""===========测试序列化============"""


def test_one_book():
    # 1,获取书籍对象
    book = BookInfo.objects.get(id=1)

    # 2,创建序列化器对象, instance=book 表示将哪一本数据进行序列化
    serializer = BookInfoSerializer(instance=book)
    # 3,输出序列化之后的结果
    print(serializer.data)


def test_many_book():
    # 1,查询所有的书籍
    books = BookInfo.objects.all()

    # 2,创建序列化器对象,many=True 表示传入的是列表对象(多个数据)
    serializer = BookInfoSerializer(instance=books, many=True)

    # 3,输出序列化的结果
    print(serializer.data)


def test_one_hero():
    hero = HeroInfo.objects.get(id=1)
    serializer = HeroInfoSerializer(instance=hero)
    data = serializer.data
    print(data)


def test_many_hero():
    heros = HeroInfo.objects.all()
    serializer = HeroInfoSerializer(instance=heros, many=True)
    data = serializer.data
    print(data)


"""============测试反序列化=============="""


def test_serializer():
    # 1,准备字典数据
    data_dict = {
        "b_title": "金瓶x-插画版",
        "b_pub_date": "2011-01-01",
        "b_read": 15,
        "b_comment": 10
    }
    # 2,创建序列化器对象
    serializer = BookInfoSerializer(data=data_dict)
    # 3,校验, raise_exception=True, 校验不通过,抛出异常信息
    # serializer.is_valid()
    try:
        serializer.is_valid(raise_exception=True)
    except Exception as e:
        print(str(e))


def test_create():
    data_dict = {
        "b_title": "金瓶x-插画版",
        "b_pub_date": "2019-01-01",
        "b_read": 15,
        "b_comment": 10
    }
    serializer = BookInfoSerializer(data=data_dict)
    serializer.is_valid(raise_exception=True)
    serializer.save()


def test_update():
    data_dict = {
        "b_title": "金瓶xxx-连环画",
        "b_pub_date": "2020-01-01",
        "b_read": 30,
        "b_comment": 20
    }
    book = BookInfo.objects.get(id=8)
    serializer = BookInfoSerializer(instance=book, data=data_dict)
    serializer.is_valid(raise_exception=True)
    serializer.save()


"""============测试ModelSerializer========="""


def test_model_serializer():
    book = BookInfo.objects.get(id=1)
    serializer = BookInfoModelSerializer(instance=book)
    data = serializer.data
    print(data)

    books = BookInfo.objects.all()
    serializer = BookInfoModelSerializer(instance=books, many=True)
    print(serializer.data)


def test_create_model_serializer():
    data_dict = {
        "b_title": "鹿鼎记",
        "b_pub_date": "2020-01-01",
        "b_read": 30,
        "b_comment": 20
    }
    serializer = BookInfoModelSerializer(data=data_dict)
    serializer.is_valid(raise_exception=True)
    serializer.save()


def test_update_model_serializer():
    data_dict = {
        "b_title": "鹿鼎记2",
        "b_pub_date": "2020-01-01",
        "b_read": 30,
        "b_comment": 20
    }
    book = BookInfo.objects.get(id=9)
    serializer = BookInfoModelSerializer(instance=book, data=data_dict)
    serializer.is_valid(raise_exception=True)
    serializer.save()
