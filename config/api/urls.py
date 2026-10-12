from rest_framework.routers import  DefaultRouter
from .views import (JobViewSet, CommentViewSet, CategoryViewSet, CategoryWithJobsViewSet,
                    CategoryDetailWithJobsViewSet)

router = DefaultRouter()

router.register('jobs', JobViewSet, basename="ishlar")
router.register('category', CategoryViewSet, basename="katagoryalar"),
router.register('comment', CommentViewSet, basename="kommentariyalar"),
router.register('categories_and_jobs', CategoryWithJobsViewSet),
router.register(
        'api/categories/<int:pk>/', CategoryDetailWithJobsViewSet, basename='category-detail-jobs')

urlpatterns = router.urls