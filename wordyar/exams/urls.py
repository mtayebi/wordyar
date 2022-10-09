import imp
from django.urls import path
from .views import UserExam, UserExamInterface

app_name = 'exams'

urlpatterns = [
    path('exam/<int:pk>/', UserExam.as_view(), name='exam'),
    path('userexaminterface/', UserExamInterface.as_view(), name='userexaminterface'),
]