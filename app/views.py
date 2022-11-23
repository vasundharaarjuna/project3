from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('this is our first  in my django class attending at jspiders')
def purpose(request):
    return HttpResponse('<marquee>yes this is mounika</marquee>'),
def school(requset):
    return HttpResponse('<marquee>school timing are already started.<br>still ur are waiting for ur friend outside</marquee>') ,

