from django.urls import path
from .views import Register
from . import views

urlpatterns = [
    path('api/register/', Register.as_view(), name='register'),
    path('api/saveit', views.Saveit, name='saveit'),
    path('requests/create/', views.create_request, name='create_request'),
    path('requests/', views.list_requests, name='list_requests'),
    path('requests/manage/<int:request_id>/', views.manage_request, name='manage_request'),
]
