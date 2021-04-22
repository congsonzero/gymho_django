from django.conf.urls import url
from gymho import views
from rest_framework_simplejwt import views as jwt_views

from gymho.views import UserRegisterView, CustomerView

urlpatterns = [
    url(r'^api/exercises$', views.ExerciselistView),
    url(r'^api/exercise/(?P<pk>[0-9]+)$', views.exercise_detail),
    url(r'^api/exercise/published$', views.exercise_list_published),
    url('api/login$', jwt_views.TokenObtainPairView.as_view(), name='login'),
    url('api/register$', UserRegisterView.as_view(), name='register'),
    url('api/customer$', CustomerView.as_view(), name='customer'),

]
