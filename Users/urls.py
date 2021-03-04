from django.urls import path

from Users.views import reg_form

urlpatterns = [
    path('register/', reg_form),
    path('login/', login_form),
]