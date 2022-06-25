from django.conf.urls import url
from rest_framework.authtoken import views
from users import views
from django.urls import path

urlpatterns = [
    url(r'signup/', views.RegisterUsers.as_view()),
    path('update-account/<username>/', views.UserDetails.as_view()),
    path('my-account/<username>/', views.UserDetails.as_view()),
    path('delete-account/<username>/', views.UserDetails.as_view()), 
]