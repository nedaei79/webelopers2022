from django.urls import path

from Users.views import reg_form, login_form, logout_user

urlpatterns = [
    path('register/', reg_form),
    path('login/', login_form),
    path('logout/', logout_user)
]