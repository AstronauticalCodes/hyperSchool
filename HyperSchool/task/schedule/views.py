from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from .models import Course
from .forms import SearchForm
# Create your views here.


def index(request):
    return HttpResponse(f'''
    <a href="/schedule/main"><button>Go to main page</button></a>
''')
    # return redirect('schedule/main')


class MainView(View):
    template_name = "schedule/main.html"
    model = Course

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     pass


    def get(self, request, *args, **kwargs):
        # print(courses, 'jello')
        try:
            search = request.GET['search']
            all_courses = self.model.objects.all()
            found_courses = [course for course in all_courses if search in course.title.lower()]
            print(found_courses, len(found_courses))
            search_found = True if len(found_courses) > 0 else False
        except Exception:
            search_found = False
            found_courses = []

        return render(request, self.template_name, context={"courses": found_courses, "search_found": search_found})


    def post(self, request, *args, **kwargs):
        # return render(request, self.template_name, context={'search_found': search_found, 'courses': found_courses})
        pass


def MainPage(request):
    # query = request.GET.get('query')
    # query = None
    found_courses = []
    # if 'query' in request.GET:
    #     form = SearchForm(request.GET)
    #     if form.is_valid():
    #         query = form.cleaned_data['query']
    #         found_courses = Course.objects.filter(title__icontains=query)
    #
    # else:
    #     form = SearchForm()

    form = SearchForm(request.POST or None)
    found_courses = []
    if request.method == 'POST' and form.is_valid():
        query = form.cleaned_data.get('query')
        found_courses = Course.objects.filter(title__icontains=query)

    return render(request, 'schedule/main.html', context={'form': form, 'courses': found_courses})