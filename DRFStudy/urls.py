from django.conf.urls import url
from rest_framework import routers

from DRFStudy.views import book_test_view, book_drf_view, api_view, generic_api_view, mixin_generic_api_view, \
    third_view, view_set_view, model_view_set

router = routers.DefaultRouter()
router.register("books", book_drf_view.BookViewSet, basename="drf_books")
router.register("book_info", model_view_set.BookInfoModelViewSet, basename="book_info")

urlpatterns = [
    url(r'^test_books/$', book_test_view.BooksAPIVIew.as_view()),
    url(r'^test_books/(?P<pk>\d+)/$', book_test_view.BookAPIView.as_view()),

    url(r'^api_books/$', api_view.BookListAPIView.as_view()),
    url(r'^api_books/(?P<book_id>\d+)/$', api_view.BookDetailAPIView.as_view()),

    url(r'^generic_api_books/$', generic_api_view.BookListGenericAPIView.as_view()),
    url(r'^generic_api_books/(?P<pk>\d+)/$', generic_api_view.BookDetailGenericAPIView.as_view()),

    url(r'^mixin_generic_api_books/$', mixin_generic_api_view.BookListMixinGenericAPIView.as_view()),
    url(r'^mixin_generic_api_books/(?P<book_id>\d+)/$', mixin_generic_api_view.BookDetailMixinGenericAPIView.as_view()),

    url(r'^third_view/$', third_view.BookListThirdView.as_view()),
    url(r'^third_view/(?P<pk>\d+)/$', third_view.BookDetailThirdView.as_view()),

    url(r'^view_set/$', view_set_view.BookViewSet.as_view({"get": "list"})),
    url(r'^view_set/(?P<pk>\d+)/$', view_set_view.BookViewSet.as_view({"get": "retrieve"})),

    url(r'^readonly_view_set/$', view_set_view.BookReadOnlyModelViewSet.as_view({"get": "list"})),
    url(r'^readonly_view_set/(?P<pk>\d+)/$', view_set_view.BookReadOnlyModelViewSet.as_view({"get": "retrieve"})),

    url(r'^model_view_set/$', view_set_view.BookModelViewSet.as_view({"get": "list", "post": "create"})),
    url(r'^model_view_set/(?P<pk>\d+)/$',
        view_set_view.BookModelViewSet.as_view({"get": "retrieve", 'put': 'update', 'delete': 'destroy'})),
    url(r'^model_view_set/bread_book/$', view_set_view.BookModelViewSet.as_view({"get": "bread_book"})),
    url(r'^model_view_set/update_partial_book_bread/(?P<pk>\d+)/$',
        view_set_view.BookModelViewSet.as_view({"put": "update_partial_book_bread"})),

]
urlpatterns += router.urls
