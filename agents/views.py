from django.shortcuts import render

from .models import Agent


# Create your views here.

def agent_list(request):
    agent_list = Agent.objects.all()
    template = 'agents/agent.html'
    context = {
        'agent_list': agent_list
    
    }

    return render(request , template , context ) 
