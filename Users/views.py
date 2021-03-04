from django.contrib.auth.models import User
from django.shortcuts import render


def reg_form(request):
    if request.method == "POST":
        inf = request.POST
        # print("************************")
        # print(inf)
        # print(inf.get("username"))
        user = User.objects.create_user(
            first_name=inf.get("first_name"),
            last_name=inf.get("last_name"),
            username=inf.get("username"),
            email=inf.get("email"),
            password=inf.get("password1")
        )

        # User.save()
        # if request.POST.get("submit"):

    return render(request=request, template_name='users/registerForm.html', context={})
