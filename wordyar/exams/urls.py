import imp
from django.urls import path
from .views import UserExam, UserExamInterface

app_name = 'exams'

urlpatterns = [
    path('exam/<str:username>/', UserExam.as_view(), name='exam'),
    path('userexaminterface/', UserExamInterface.as_view(), name='userexaminterface'),
]