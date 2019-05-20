from django.contrib import admin
from django.urls import path, include
from .views import TodoCreateView, TodoListView, TodoRetrieveUpdateDestroyView, TodoOverdueListView

urlpatterns = [
    path('', TodoListView.as_view()),
    path('create/', TodoCreateView.as_view()),
    path('<int:pk>/', TodoRetrieveUpdateDestroyView.as_view()),
    path('overdue/', TodoOverdueListView.as_view()),
]
