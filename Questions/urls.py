from django.urls import path, include
from .views import QuestionsViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('question', QuestionsViewset)
urlpatterns = [
    path('', include(router.urls))
]
