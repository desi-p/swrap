from django.urls import URLPattern, path

from swrapproj import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update_course/int:pk>', views.courseUpdate, name = 'courseUpdate'),
]