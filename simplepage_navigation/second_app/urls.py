from django.urls import  path
from . import views

urlpatterns = [
    path('course/',views.course),
    path('teacher/',views.teacher)
]