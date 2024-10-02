from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student_list/', views.student_list, name='student_list'),
    path('student_list/<int:pk>/', views.student_detail, name='student_detail'),
    #path('', views.student_list, name='student_list'),
]