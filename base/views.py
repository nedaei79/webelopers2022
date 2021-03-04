from django.http import HttpResponse
from django.shortcuts import render


def navbar(request):
    return HttpResponse(content="hi")


def home(request):
    return render(request=request, template_name='mainpage/main_page.html', context={})


def contact_us(request):
    if request.method == "POST":
        inf = request.POST
        text = str(inf.get('text'))
        # print("*********************************")
        # print(len(text), text)
        if 10 <= len(text) <= 250:
            return render(request=request, template_name='pages/successful.html', context={})

    return render(request=request, template_name='pages/contact_us.html', context={})
