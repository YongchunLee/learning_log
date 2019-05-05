"""
* date：2019/4/30 0030
* time：上午 11:36
__author__ = "lyc"

"""
from django.urls import path,re_path
from . import views


app_name = "learning_logs"
urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    # path('topics/<topic_id>/', views.topic, name='topic'),
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # 用于添加新主题的网页
    path('new_topic/', views.new_topic, name='new_topic'),
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name="new_entry"),
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name="edit_entry"),
]