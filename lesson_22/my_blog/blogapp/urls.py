from django.urls import path
from blogapp import views


app_name = 'blogapp'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('post/<int:id>/', views.post, name='post'),
    path('create_post/', views.create_post, name='create_post'),
]