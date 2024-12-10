from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from schedule.forms import SignUpForm


def index(request):
    return HttpResponse(f'''
    <a href="/schedule"><button>Go to schedule page</button></a>
''')
    # return redirect('schedule/main')


class HyperSchoolLoginView(LoginView):
    template_name = "login.html"
    success_url = '/'
    form = AuthenticationForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'form': self.form})


class HyperSchoolSignUpView(CreateView):
    template_name = "signup.html"
    success_url = "login"
    form = UserCreationForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'form': self.form})

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.refresh_from.db()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('login')
        else:
            print('not valid')
            return HttpResponse("<h2>not vaild</h2>")


def LogOut(request):
    logout(request)
    return redirect('schedule/main')