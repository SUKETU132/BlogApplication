from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path("", views.fetch_data, name="fetch_data"),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_page, name="logout"),
    path("register/", views.register, name="register"),
    path("mypost/", views.view_user_post, name="view_user_post"),
    path('add/', views.add_post, name='add_post'),
    path('edit/<int:id>/', views.edit_post, name='edit_post'),
    path('delete/<int:id>/', views.delete_post, name='delete_post'),
]
