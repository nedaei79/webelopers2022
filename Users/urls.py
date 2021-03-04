from django.urls import path

from Users.views import reg_form

urlpatterns = [
    path('register/', reg_form),
]