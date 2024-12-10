from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import CreateView, FormView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from schedule.forms import SignUpForm
from django.views import View


def index(request):
    return HttpResponse(f'''
    <a href="/schedule"><button>Go to schedule page</button></a>
''')


def LogOut(request):
    logout(request)
    return redirect('../schedule/main')


class HyperSchoolSignUpView(View):
    template_name = 'signup.html'
    form = SignUpForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        return render(request, self.template_name, context={'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        print(form.is_valid)
        if form.is_valid():
            form.save()
            return redirect('/schedule/main')
        else:
            print('not valid')
            return HttpResponse("<h2>Not Valid</h2>")


class HyperSchoolLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True