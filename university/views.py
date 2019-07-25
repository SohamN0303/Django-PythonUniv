from django.shortcuts import render
from .models import about

# Create your views here.
def index(request):

    aboutus= about.objects.all()
    return render(request, "index.html",{'aboutus':aboutus})