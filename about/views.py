from django.shortcuts import render
from .models import About
# Create your views here.

def about_us(request):
    about_us_content = About.objects.last()
    template = 'about/about.html'
    context = {

        'about_us' : about_us_content
    }

    return render(request,template,context)