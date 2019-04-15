from django.http import HttpResponse
from django.shortcuts import render
import datetime

def home(request):
	return render(request,'home.html')

def login(request):
	return render(request,'login.html')

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
	
def blackhole(request):
	return render(request,'hole.html')