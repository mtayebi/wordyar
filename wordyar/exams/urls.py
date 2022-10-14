from django.urls import path
from .views import UserExam, UserExamInterface, AjaxResponse

app_name = 'exams'

urlpatterns = [
    path('exam/<int:pk>/', UserExam.as_view(), name='exam'),
    path('userexaminterface/', UserExamInterface.as_view(), name='userexaminterface'),
    path('api/', AjaxResponse.as_view(), name='ajaxresponse'),

]