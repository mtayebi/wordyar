
import random
from django.shortcuts import redirect, render, HttpResponse
from django.views import View
from core.models import BaseUser
from .models import Exam, Question
from .forms import ExamForm
from accounts.models import Account
from django.contrib.auth.mixins import LoginRequiredMixin


# Create exam views and mange logic that user can take exam 

class UserExamInterface(LoginRequiredMixin, View):

    """
    this class just is an interface between home page and user page
    the user can custom values like exam number of questions and level
    of exam then exam will create and the page of exam will load appropriately
    """

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
            exam = Exam.objects.create(account=account, number=form.get('number', 10))
            return redirect('exams:exam', exam.pk)



class UserExam(LoginRequiredMixin, View):
    
    template_name = 'exams/exam.html'
    random_choices = [0, 1 ,2, 3]

    def get(self, request, pk):
        questions = list(Question.objects.all())
        questions = random.sample(questions, 4)
        random_choice = random.sample(self.random_choices, 4)

        context = {
            'question':questions[0].question,
            'answers': [question.answer for question in questions]
        }
        return render(request, self.template_name, context=context)


    def post(self, request, *args, **kwargs):

        user = request.user
        account = Account.objects.get(user=user)
        exam = Exam.objects.filter(account=account).last()

        if exam.question_passed < exam.number:
            exam.question_passed += 1
            exam.save()
            print("="*100)
            print(request.POST['1'], request.POST, exam.question_passed, exam.number)
            return redirect('exams:exam', exam.pk)
        return HttpResponse('finished')
