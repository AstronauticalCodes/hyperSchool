from django.http import HttpResponse


def index(request):
    return HttpResponse(f'''
    <a href="/schedule"><button>Go to schedule page</button></a>
''')
    # return redirect('schedule/main')