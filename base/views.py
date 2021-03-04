from django.http import HttpResponse
from django.shortcuts import render


def navbar(request):
    return HttpResponse(content="hi")


def home(request):
    return render(request=request, template_name='mainpage/main_page.html', context={})