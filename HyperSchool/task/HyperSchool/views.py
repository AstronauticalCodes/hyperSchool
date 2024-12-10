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
    # return redirect('schedule/main')


# class HyperSchoolLoginView(LoginView):
#     template_name = "login.html"
#     success_url = '/'
#     form = AuthenticationForm
#
#     def get(self, request, *args, **kwargs):
#         return render(request, self.template_name, context={'form': self.form})
#
#
# class HyperSchoolSignUpView(CreateView):
#     template_name = "signup.html"
#     success_url = "login/"
#     form = UserCreationForm
#
#     def get(self, request, *args, **kwargs):
#         return render(request, self.template_name, context={'form': self.form})
#
#     def post(self, request, *args, **kwargs):
#         form = SignUpForm(request.POST)
#
#         if form.is_valid():
#             user = form.save()
#             user.refresh_from_db()
#             print(form.cleaned_data)
#             user.save()
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=user.username, password=raw_password)
#             login(request, user)
#             return redirect('login/')
#         else:
#             print('not valid')
#             return HttpResponse("<h2>not vaild</h2>")
#
#
def LogOut(request):
    logout(request)
    return redirect('../schedule/main')


# class HyperSchoolLoginView(FormView):
#     template_name = 'login.html'
#     success_url = '/schedule/main'
#     form = AuthenticationForm
#
#     def form_valid(self, form):
#         username = form.cleaned_data['username']
#         password = form.cleaned_data['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(self.request, user)
#         return super().form_valid(form)


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
        # return render(request, self.template_name, {'form': form})


class HyperSchoolLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True