from django.conf.urls import url
from gymho import views

urlpatterns = [
    url(r'^api/exercises$', views.exercise_list),
    url(r'^api/exercise/(?P<pk>[0-9]+)$', views.exercise_detail),
    url(r'^api/exercise/published$', views.exercise_list_published)]
