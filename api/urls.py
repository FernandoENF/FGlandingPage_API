from django.urls import path, include
from .views import student_view

urlpatterns = [
    path('alunos/', student_view.StudentList.as_view(), name='student-list'),

]
