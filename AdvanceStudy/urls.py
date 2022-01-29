from django.conf.urls import url

from AdvanceStudy import views, aop_views, page_views

urlpatterns = [
    url(r"^news/$", views.news, name="news"),
    url(r"^redis_news/$", views.redis_news, name="redis_news"),

    url(r"^get_phone/$", aop_views.get_phone, name="get_phone"),
    url(r"^get_ticket/$", aop_views.get_ticket, name="get_ticket"),
    url(r"^search/$", aop_views.search, name="search"),
    url(r"^hello/$", aop_views.hello, name="hello"),

    url(r"^add_animals/$", page_views.add_animals, name="add_animals"),
    url(r"^get_animals/$", page_views.get_animals, name="get_animals"),
]
