from django.urls import path

from school.views import students_list

urlpatterns = [
    path('s_l/', students_list, name='students'),
]
