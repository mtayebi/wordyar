
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpRequest
from django.views import View
from core.models import BaseUser
from .models import Exam
from .forms import ExamForm
from accounts.models import Account
from django.contrib.auth.mixins import LoginRequiredMixin


# Create exam views and mange logic that user can take exam 

class UserExamInterface(LoginRequiredMixin, View):
    
    form_class = ExamForm
    temlate_name = 'exams/examform.html'
    

    def get(self, request):
        context={
            'form':self.form_class
        }
        return render(request, self.temlate_name, context=context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            user = request.user
            account = Account.objects.get(user=user)

            # we craete an exam for user --- level of exam ignored we will handle this later in modification
            Exam.objects.create(account=account, number=form.get('number', 10))

            return redirect('exams:exam', user.username)



class UserExam(LoginRequiredMixin, View):

    def get(self, request, username):
        user = BaseUser.objects.get(username=username)
        account = Account.objects.get(user=user)
        exam = Exam.objects.filter(account=account).last()
        return HttpResponse(exam.create_time)

    def post(self, request):
        ...
