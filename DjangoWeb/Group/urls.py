from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^new/$',views.CreateGroup.as_view(),name='create_group'),
    url(r'^$',views.AllGroups.as_view(),name='all'),
    url(r'^posts/in/(?P<pk>\d+)$', views.GroupDetail.as_view(), name='group_detail'),
    url(r'^Group/(?P<pk>\d+)/Join/$', views.JoinGroup.as_view(), name='Join'),
    url(r'^Group/(?P<pk>\d+)/Leave/$', views.LeaveGroup.as_view(), name='Leave'),
    url(r'^Group/(?P<pk>\d+)/delete/$', views.GroupDelete.as_view(), name='group_delete'),
]
