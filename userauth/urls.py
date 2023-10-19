from django.urls import path

from userauth import views

app_name = 'userauth'

urlpatterns = [
    path('sign-up/', views.register_view, name='sign-up'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

]
