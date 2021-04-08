from django.conf.urls import url
from gymho import views

urlpatterns = [
    url(r'^api/execises$', views.execise_list),
    url(r'^api/execise/(?P<pk>[0-9]+)$', views.execise_detail),
    url(r'^api/execise/published$', views.execise_list_published)]
