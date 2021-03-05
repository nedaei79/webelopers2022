from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from Users.models import product


def reg_form(request):
    if request.method == "POST":
        inf = request.POST
        try:
            user = User.objects.get(username=inf.get("username"))
            return render(request=request, template_name='users/registerForm.html', context={'err': 'u'})
        except User.DoesNotExist:
            pass1 = inf.get("password1")
            pass2 = inf.get("password2")
            if pass1 != pass2:
                return render(request=request, template_name='users/registerForm.html', context={'err': 'p'})

            user = User.objects.create_user(
                first_name=inf.get("first_name"),
                last_name=inf.get("last_name"),
                username=inf.get("username"),
                email=inf.get("email"),
                password=inf.get("password1")
            )

            user.save()

    return render(request=request, template_name='users/registerForm.html', context={'err': 'n'})


def login_form(request):
    if request.method == "POST":
        inf = request.POST
        username = inf.get("username")
        password = inf.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
        else:
            return render(request=request, template_name='users/loginForm.html', context={'err': True})
    return render(request=request, template_name='users/loginForm.html', context={'err': False})


def logout_user(request):
    logout(request)
    return redirect('/')


def user_panel(request):
    if request.method == 'POST':
        inf = request.POST
        if inf.get('become_seller'):

            if request.user.groups.filter(name='sellers').exists():
                return render(request=request, template_name='users/panel.html', context={'condition': 'error'})
            seller_group = Group.objects.get(name='sellers')
            seller_group.user_set.add(request.user)
            return render(request=request, template_name='users/panel.html', context={'condition': 'done'})

    return render(request=request, template_name='users/panel.html', context={'condition': 'null'})


def make_product(request):
    if request.method == 'POST':
        inf = request.POST
        name = inf.get('name')
        quantity = inf.get('quantity')
        price = inf.get('price')
        temp = product(name=name, quantity=quantity, price=price)
        temp.save()
    return render(request=request, template_name='users/make_product.html', context={})
