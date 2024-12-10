from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

def index(request):
    return HttpResponse(f'''
    <a href="/schedule"><button>Go to schedule page</button></a>
''')
    # return redirect('schedule/main')


class HyperSchoolLoginView(LoginView):
    template_name = "login.html"
    success_url = 'schedule/main'
    form = AuthenticationForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'form': self.form})