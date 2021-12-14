from django.urls import path, include
from .views import QuestionsViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', QuestionsViewset)
urlpatterns = [
    path('', include(router.urls))
]
