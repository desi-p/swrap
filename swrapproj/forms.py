from django import forms
from .models import Course

#form class -- import class Course
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'course_provider', 'course_completed', 'certificate_earned']