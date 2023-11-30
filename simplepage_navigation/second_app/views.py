from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def course(request):
    return HttpResponse('''<h1>thia is course page</h1>
                           <a href='/first_app/contact/'>contact</a>
                           <a href='/first_app/about/'>about</a>
                           <a href='/second_app/teacher/'>teacher</a>
                           
                        ''')
def teacher(request):
    return HttpResponse('''<h1>thia is teacher page</h1>
                           <a href='/first_app/contact/'>contact</a>
                           <a href='/first_app/about/'>about</a>
                           <a href='/second_app/course/'>teacher</a>
                        ''')