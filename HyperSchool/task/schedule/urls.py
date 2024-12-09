from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # path('schedule/main/', views.MainView.as_view()),
    path('main/', views.MainPage, name='main'),
    path('course_details/<int:pk>/', views.MainPage, name='main'),
    path('teacher_details/<int:pk>/', views.MainPage, name='main'),
]