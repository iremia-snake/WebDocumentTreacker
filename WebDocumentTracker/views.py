from django.shortcuts import render
from django.http import HttpResponse

def auth(request):
    data = {

    }
    return render(request, 'WebDocumentTracker/authorization.html', data)
def index(request):
    return HttpResponse("<h1>Привет, мир!</h1>")
# Create your views here.
