from django.shortcuts import render
from django.http import HttpResponse

def auth(request):
    data = {
        'values':[1,2,3,4,5,6,7,8,9,0]
    }
    return render(request, 'WebDocumentTracker/authorization.html', data)
def index(request):
    return HttpResponse("<h1>Привет, мир!</h1>")
# Create your views here.
