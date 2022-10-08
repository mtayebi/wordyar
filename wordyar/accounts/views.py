from accounts.models import Account
from django.shortcuts import redirect, render
from django.views import View
from accounts.forms import AccountForm, LoginForm
from core.models import BaseUser
from django.contrib import messages
from django.contrib.auth import login, authenticate



# define accounts views containing registeration and uer profile


class UserRegister(View):
    form_class = AccountForm
    template_name = 'accounts/register.html'

    # show registeration form to user
    def get(self, request):
        context = {'form':self.form_class}
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # get clean data of form that user posted as a dictionary
            form = form.cleaned_data

            # create user according to form that user filled and post to us
            user = BaseUser.objects.create_user(username=form['username'],
                password=form['password'], email=form['email'], phone=form.get('phone', None))

            # creat account according to new user registered
            Account.objects.create(user=user)

            # login user and kept login
            login(request, user)

            # send suuccess message it will be handeled in 'inc/messages.html'
            messages.success(request, 'کاربر با موفقیت ساخته شد', 'info')

            # send user to home for continue his/her operation
            return redirect('core:home')

        # if form was invalid show registration page again by form errors
        return render(request, self.template_name, {"form": form})

class Login(View):
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def get(self, request):
        context= {
            'form':self.form_class,
        }
        
        return render(request, self.template_name, context=context)

    def post(self, request):
        ...