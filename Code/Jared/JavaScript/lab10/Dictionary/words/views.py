from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
import json
from .secrets import API_KEYS

# Create your views here.
def dictionary(request):
	return render(request, 'words/lab10.html')

def api_keys(request):
	return JsonResponse(API_KEYS)