from django.urls import path
from django.contrib.auth.views import LogoutView

from userapp import views

app_name = 'userapp'

urlpatterns = [
    path('registration/', views.UserCreateView.as_view(), name='regist'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]