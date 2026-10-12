from rest_framework import serializers, generics
from .models import Job, Comment, Category


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class JobSerializerForCourse(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['salary']


class CategorySerializerForDetail(serializers.ModelSerializer):
    jobs = JobSerializerForCourse(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id']

class CatSer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['type']


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['id', 'user', 'username', 'text', 'created_at']
        read_only_fields = ['user', 'created_at']

class CategoryWithJobsSerializer(serializers.ModelSerializer):
    jobs = JobSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'type', 'durations', 'jobs']



