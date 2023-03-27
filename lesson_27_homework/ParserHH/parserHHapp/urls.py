from django.urls import path
from parserHHapp import views

app_name = 'parserHHapp'

urlpatterns = [
    path('', views.start, name='index'),
    path('form/', views.form, name='form'),
    path('about/', views.about, name='about')
]