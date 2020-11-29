from django.shortcuts import render
from property.models import Category,Property
from agents.models import Agent 
from django.db.models import Count




# Create your views here.

def home(request):
    template = 'home/home.html'
    category_list =  Category.objects.annotate(pr_count= Count('property') )
    
    
    property_list = Property.objects.all()
    agent_list = Agent.objects.all()



    context = {
        'category_list_home':category_list,
        'property_list_home':property_list,
        'agent_list_home': agent_list

    }

    return render(request,template,context)
