from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


    def create(self,validated_data):
        return Task.objects.create(**validated_data)
    
    
    def update(self, instance, validated_data):
        
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description',instance.description)
        instance.status = validated_data.get('status',instance.description)
        instance.save()
        return instance
    
