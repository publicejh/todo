from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Todo


class TodoListSerializer(serializers.ModelSerializer):
    priority_name = serializers.SerializerMethodField()
    deadline_str = serializers.SerializerMethodField()

    def get_priority_name(self, obj):
        return obj.priority_name()

    def get_deadline_str(self, obj):
        return obj.deadline_str()

    class Meta:
        fields = ('id', 'todo_title', 'todo_content', 'deadline', 'status', 'priority', 'is_deleted', 'modified_time',
                  'priority_name', 'deadline_str')
        model = Todo
