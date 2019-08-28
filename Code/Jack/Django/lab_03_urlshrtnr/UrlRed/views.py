from django.shortcuts import render
from django.http import HttpResponse

def <view name>(request):
    context = {}
    return render(request, 'UrlRed/index.html', context)
    # return HttpResponse(status=204)