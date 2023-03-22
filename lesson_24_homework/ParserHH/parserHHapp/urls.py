from django.urls import path
from parserHHapp import views

app_name = 'parserHHapp'

urlpatterns = [
    path('', views.start, name='index'),
    path('form/', views.form, name='form'),
    path('result/', views.result, name='result'),
    path('ws-list/', views.WSList.as_view(), name='ws_list'),
    path('area-list/', views.AreaList.as_view(), name='area_list'),
    path('area-detail/<int:pk>/', views.AreaDetail.as_view(), name='area_detail'),
    path('area-create/', views.AreaCreate.as_view(), name='area_create'),
    path('area-update/<int:pk>/', views.AreaUpdateView.as_view(), name='area_update'),
    path('area-delete/<int:pk>/', views.AreaDeleteView.as_view(), name='area_delete')
]