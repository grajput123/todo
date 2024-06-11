from django.urls import path
from . import views

urlpatterns = [
    path('form_view/', views.todo_view, name='todo_create'),
    path('show_view/', views.show_view, name='todo_show'),
    path('update_view/<int:pk>/', views.update_view, name='todo_update'),
    path('delete_view/<int:pk>/', views.delete_view, name='todo_delete'),
]