from . import views
from django.urls import path, register_converter
from .converters import YearConverter, MonthConverter, DayConverter

register_converter(YearConverter, 'year') 
register_converter(MonthConverter, 'month') 
register_converter(DayConverter, 'day') 

app_name = 'instagram' # url reverse에서 namespace 역할을 함

urlpatterns = [
    path('new/', views.post_new, name='post_new'),
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('archive/', views.post_archive, name='post_archive'),
    path('archive/<year:year>/', views.post_archive_year, name='post_archive_year)'),
    ]