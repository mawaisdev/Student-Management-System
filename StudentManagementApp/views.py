from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def showDemoPage(request):
    return render(request, "index.html")


def Home(request):
    return HttpResponse("HOME")