from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
# Create your views here.


def index(request):
    return HttpResponse(f'''
    <a href="/schedule/main"><button>Go to main page</button></a>
''')
    # return redirect('schedule/main')


class MainView(View):
    def get(self, request):
        return render(request, "schedule/main.html")
    pass