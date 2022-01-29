from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render

from ViewStudy.models import Grade, Student


def hello_world(request):
    return HttpResponse("hello world...")


def students(request):
    return HttpResponse("Get Students Success")


def student(request, s_id):
    student_list = Student.objects.filter(s_grade_id=s_id)
    return render(request, 'grade_student_list.html', context=locals())


def grades(request):
    grade_list = Grade.objects.all()
    return render(request, 'grade_list.html', context=locals())


def get_date(request, day, month, year):
    return HttpResponse("Date %s-%s-%s" % (year, month, day))


def learns(request):
    return HttpResponse("learns")
