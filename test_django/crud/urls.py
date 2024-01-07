from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='display'),
    path('display/', views.crud, name='display'),
    path('insert/', views.insert_view, name='insert'),
    path('edit/<int:id>/', views.edit_view, name='edit'),  
    path('delete/<int:id>/', views.delete_view, name='delete'), 
]
