from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


def reg_form(request):
    form = UserCreationForm()
    return render(request=request, template_name='users/registerForm.html', context={'form': form})
