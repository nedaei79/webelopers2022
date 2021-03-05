from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from ssc.settings import EMAIL_HOST_USER
from Users.models import product
from django.contrib.auth.models import User

def navbar(request):
    return HttpResponse(content="hi")


def home(request):
    return render(request=request, template_name='mainpage/main_page.html', context={})


def contact_us(request):
    if request.method == "POST":
        inf = request.POST
        title = str(inf.get('title'))
        email = str(inf.get('email'))
        text = str(inf.get('text'))
        # print("*********************************")
        # print(len(text), text)
        if 10 <= len(text) <= 250:
            send_mail(title, email + '\n' + text, EMAIL_HOST_USER, ['nedaei79@gmail.com'], fail_silently=False,)
            return render(request=request, template_name='pages/successful.html', context={})

    return render(request=request, template_name='pages/contact_us.html', context={})


def all_products(request):
    products = product.objects.all()
    manip_products = [(temp,
                       (temp.name + ' ' + temp.seller_username).replace(' ', '_'),
                       User.objects.get(username=temp.seller_username).first_name,
                       User.objects.get(username=temp.seller_username).last_name) for temp in products]
    return render(request=request, template_name='pages/all_products.html', context={'products': manip_products})
