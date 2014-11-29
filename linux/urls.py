from django.conf.urls import patterns, include, url
from .views import DistroCreate, DistroUpdate, DistroDelete,DistroList

urlpatterns = patterns('',

    url(r'^$', DistroList.as_view(), name='distro_lista'),
    url(r'distro/add/$', DistroCreate.as_view(), name='distro_add'),
    url(r'distro/(?P<pk>\d+)/$', DistroUpdate.as_view(), name='distro_update'),
    url(r'distro/(?P<pk>\d+)/delete/$', DistroDelete.as_view(), name='distro_delete'),
)
