from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'Threadly/index.html')

def base(request):
    return render(request, 'Threadly/base.html')

def hi(request):
    return HttpResponse("Hello, This is an initialization page<br>"
                        "<a href='/Threadly/index/'>Index</a><br>" 
                        "<a href='/Threadly/'>Base</a>")## This is an initialization page for displaying existing pages