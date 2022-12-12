from django.urls import path
from .views import (TaskListView, TaskDetailView, CreateTaskView, DeleteTaskView,
                    UpdateTaskView, CustomerLogin, RegisterPage)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',CustomerLogin.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('register/',RegisterPage.as_view(),name='register'),
    
    path('',TaskListView.as_view(),name='tasks'),
    path('task/<int:pk>',TaskDetailView.as_view(),name='task'), 
    path('create/',CreateTaskView.as_view(),name='create'),
    path('delete/<int:pk>',DeleteTaskView.as_view(),name='delete'),
    path('update/<int:pk>',UpdateTaskView.as_view(),name='update'),
    
    
    
    
]