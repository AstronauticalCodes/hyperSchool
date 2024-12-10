from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from .models import Course, Teacher, Student
from .forms import SearchForm, StudentForm


def index(request):
    return HttpResponse(f'''
    <a href="/schedule/main"><button>Go to main page</button></a>
''')


class MainView(View):
    template_name = "schedule/main.html"
    model = Course

    def get(self, request, *args, **kwargs):
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


def MainPage(request):
    form = SearchForm(request.POST or None)
    found_courses = []
    if request.method == 'GET':
        print(request.user.is_authenticated)
    if request.user.is_authenticated:
        # print(request.user.name)
        pass
    if request.method == 'POST' and form.is_valid():
        query = form.cleaned_data.get('query')
        found_courses = Course.objects.filter(title__icontains=query)

    return render(request, 'schedule/main.html', context={'form': form, 'courses': found_courses})


class CourseDetailsView(View):
    template_name = "schedule/course_details.html"
    model = Course

    def get(self, request, pk, *args, **kwargs):
        pk = self.kwargs['pk']
        course = self.model.objects.filter(id=pk).first()
        return render(request, self.template_name, context={'course': course, 'teachers': course.teacher.all()})


class TeacherDetailsView(View):
    template_name = 'schedule/teacher_details.html'
    model = Teacher

    def get(self, request, pk, *args, **kwargs):
        pk = self.kwargs['pk']
        teacher = self.model.objects.filter(id=pk).first()
        return render(request, self.template_name, context={'teacher': teacher})


class AddCourseView(View):
    template_name = 'schedule/add_course.html'
    model = Student
    form = StudentForm


    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'form': self.form})


    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('./')