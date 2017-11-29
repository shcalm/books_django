from django.conf.urls import url
from . import  views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index',views.index),
    url(r'^book/(?P<book_id>[0-9]+)', views.book_detail, name='bookdetail'),
    url(r'^login',views.login,name='login'),
    url(r'^register',views.register,name='register'),
    url(r'^doregister',views.doregister,name="doregister")

]

