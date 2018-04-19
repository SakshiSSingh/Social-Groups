from django.conf.urls import url
from . import views

app_name='posts'

urlpatterns=[
    url(r'^new/$',views.CreatePost.as_view(),name='create_post'),
    url(r'^$',views.PostList.as_view(),name='all'),

    url(r'^by/(?P<username>[-\w]+)/(?P<pk>\d+)/$',views.PostDetail.as_view(), name='post_detail'),
    url(r"delete/(?P<pk>\d+)/$",views.PostDelete.as_view(),name="delete"),
]
