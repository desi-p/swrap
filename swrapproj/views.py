from django.shortcuts import render, redirect

from .forms import CourseForm
from .models import Course
from django.http import HttpResponse


def index(request):
    courses = Course.objects.all()
    form = CourseForm()
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'index.html', {'courses': courses, 'form': form})

def courseUpdate(request, pk):
    course = Course.objects.get(id = pk)
    updateForm = CourseForm(instance = course)
    if request.method == 'POST':
        updateForm = CourseForm(request.POST, instance = course)
        if updateForm.is_valid():
            updateForm.save()
            return redirect ('index')
    return render(request, 'courseupdate.html', {'course': course, 'updateForm': updateForm})
