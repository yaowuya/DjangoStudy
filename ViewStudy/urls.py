from django.conf.urls import url

from ViewStudy import views, cookie_view, session_view, token_view

urlpatterns = [
    url(r'^hello_world$', views.hello_world),
    url(r'^students/$', views.students),
    url(r'^students/(\d+)/$', views.student),
    url(r'^grades/$', views.grades),
    url(r'^get_date/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$', views.get_date, name="get_date"),
    url(r"^learn/$", views.learns, name="learn"),

    url(r"^set_cookie/$", cookie_view.set_cookie),
    url(r"^get_cookie/$", cookie_view.get_cookie),
    url(r"^login/$", cookie_view.login, name="login"),
    url(r"^do_login/$", cookie_view.do_login, name="do_login"),
    url(r"^mine/$", cookie_view.mine, name="mine"),
    url(r"^logout/$", cookie_view.logout, name="logout"),

    url(r"^session_login/$", session_view.session_login, name="session_login"),
    url(r"^session_mine/$", session_view.session_mine, name="session_mine"),
    url(r"^session_logout/$", session_view.session_logout, name="session_logout"),

    url(r"^register/$", token_view.register, name="register"),
    url(r"^student_login/$", token_view.student_login, name="student_login"),
    url(r"^student_mine/$", token_view.student_mine, name="student_mine"),

]
