from django.shortcuts import render
from .chat_gpt import get_chat_response
from django.http import HttpResponse
import json
from src.demo.models import STI

# Create your views here.

def title(request):
    return render(request, "title.html")
def index(request):
    return render(request, "index.html")
def plan(request):
    return render(request, "plan.html")

def chat_gpt(request):
    
    response = get_chat_response(request.GET.get('input'))
    

    return HttpResponse(json.dumps(response), content_type='application/json')
