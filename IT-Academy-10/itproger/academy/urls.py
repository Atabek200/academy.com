from django.urls import path
from django.views.generic import TemplateView

from . import views
from .views import master_signup, client_signup

urlpatterns = [
    path('', views.main, name='home'),
    path('index/', views.index, name='index'),
    path('signup/master/', master_signup, name='master_signup'),
    path('signup/client/', client_signup, name='client_signup'),

    path('ticket_list/', views.client_list, name='ticket_list'),
    path('<int:pk>/', views.client_detail, name='ticket_detail'),
    path('create/', views.client_create, name='ticket_create'),


    path('master_list/', views.master_list, name='master_list'),
    path('deteil/master/<int:pk>/', views.master_detail, name='master_detail'),
    path('<int:pk>/update/', views.master_update, name='master_update'),


    path('logins/', views.login_view, name='login'),
    path('master/', TemplateView.as_view(template_name='master_page.html'), name='master_page'),
    path('client/', TemplateView.as_view(template_name='client_page.html'), name='client_page'),
]
