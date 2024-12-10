from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # path('schedule/main/', views.MainView.as_view()),
    path('main/', views.MainPage, name='main'),
    path('course_details/<int:pk>', views.CourseDetailsView.as_view(), name='course_details'),
    path('teacher_details/<int:pk>', views.TeacherDetailsView.as_view(), name='teacher_details'),
]