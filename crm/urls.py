from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
#    path("login_user/", views.login_user, name="login_user"),
    path("logout_user/", views.logout_user, name="logout_user"),
    path("register_user/", views.register_user, name="register_user"),
    path("customer/<int:pk>", views.customer_data, name="customer_data"),
    path("del_cst/<int:pk>", views.del_cst, name="del_cst"),
    path("add_customer/", views.add_customer, name="add_customer"),
    path("update_customer/<int:pk>", views.update_customer, name="update_customer"),
]

'''
it works without the "login_user/" path
reason:
it is "wired" inside the home view's authentication

if you wish, you can separate the login_user view,
and code it's function/definition separately
'''
