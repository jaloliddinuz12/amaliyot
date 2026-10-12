
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .models import Job, Category, Comment
from .serializers import  CategorySerializerForDetail, JobSerializer, CommentSerializer, CategoryWithJobsSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializerForDetail



class StudentViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
# ===============================================

class GenreViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializerForDetail

    def get_serializer_class(self):
        if self.kwargs.get("pk"):
            return CategorySerializerForDetail
        return JobSerializer




class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CategoryWithJobsViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryWithJobsSerializer
from rest_framework import viewsets



class CategoryDetailWithJobsViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializerForDetail
  # Add your custom logic for including jobs here