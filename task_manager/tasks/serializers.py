from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        owner = serializers.ReadOnlyField(source = 'owner.username')

    

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'tasks']