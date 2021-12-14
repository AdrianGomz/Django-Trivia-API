from rest_framework import viewsets
from .serializers import QuestionSerializer
from .models import Question
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .customPermissions import isAuthor


class QuestionsViewset(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, isAuthor]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
