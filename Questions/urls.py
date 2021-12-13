from django.urls import path, include
from .views import QuestionsViewset
from rest_framework.routers import DefaultRouter


question_list = QuestionsViewset.as_view({

    'get': 'list',
    'post': 'create'
})
question_detail = QuestionsViewset.as_view({
    'get': 'retrive',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

router = DefaultRouter()
router.register('question', QuestionsViewset)
urlpatterns = [
    path('', include(router.urls))
]
