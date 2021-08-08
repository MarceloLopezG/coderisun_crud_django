from django.conf.urls import url
from rest_framework.authtoken import views
from users import views

urlpatterns = [
    url(r'signup/', views.RegisterUsers.as_view()),
    url(r'^update/(?P<id>\d+)/', views.UserDetails.as_view()),
    url(r'^info/(?P<id>\d+)/', views.UserDetails.as_view()),
    url(r'^delete/(?P<id>\d+)/', views.UserDetails.as_view()),
]