from django.conf.urls import url
from rest_framework.authtoken import views
from login import views

urlpatterns = [
    url(r'^login/', views.Login.as_view()),
    url(r'^logout/', views.Logout.as_view()), 
]