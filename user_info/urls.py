from django.urls.conf import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'user_info'

urlpatterns=[
    path('', views.home, name = 'home'),
    path('mypage', views.mypage, name = 'mypage'),
    path('login', views.login_view, name = 'login_view'),
    path('signup', views.SignUp, name = 'SignUp'),
]