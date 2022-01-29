from django.conf.urls import url
from rest_framework import routers

from RestStudy import views, cbv_views, quickstart_rest_views

router = routers.DefaultRouter()
router.register(r'users', quickstart_rest_views.UserViewSet, basename="users")
router.register(r'groups', quickstart_rest_views.GroupViewSet, basename="groups")

urlpatterns = [
    url(r"^books/$", views.books),
    url(r"^book/(?P<book_id>\d+)", views.book),

    url(r"^cbv/books/$", cbv_views.BooksCBV.as_view()),
]
urlpatterns += router.urls
