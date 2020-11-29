from django.urls import path
from .  import views

app_name = 'agents'

urlpatterns = [
    path('', views.agent_list, name='agent_list'),
   # path('<int:id>', views.property_detail, name='property_detail'),
]
