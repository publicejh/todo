from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer, TodoListSerializer
# from rest_framework_swagger


class TodoCreateView(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoListView(generics.ListAPIView):
    queryset = Todo.objects.all().order_by('-modified_time')
    serializer_class = TodoListSerializer


class TodoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
