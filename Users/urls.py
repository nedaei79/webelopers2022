from django.urls import path

from Users.views import *

urlpatterns = [
    path('register/', reg_form),
    path('login/', login_form),
    path('logout/', logout_user),
    path('panel/', user_panel),
    path('panel/make_product/', make_product),
    path('panel/my_products', my_products),
]