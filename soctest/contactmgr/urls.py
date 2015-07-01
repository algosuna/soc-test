from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^upload/$', views.UploadView.as_view(), name='upload'),
    url(r'^$', views.ContactList.as_view(), name='contact_list'),
    url(r'^(?P<pk>\d+)/edit/$',
        views.ContactUpdate.as_view(), name='contact_update'),
    url(r'^(?P<pk>\d+)/detail/$',
        views.ContactDetail.as_view(), name='contact_detail'),
    url(r'^(?P<pk>\d+)/delete/$',
        views.ContactDelete.as_view(), name='contact_delete')
]
