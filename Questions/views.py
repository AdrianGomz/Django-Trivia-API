from rest_framework import viewsets
from rest_framework import permissions
from .serializers import QuestionSerializer
from .models import Question
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class QuestionsViewset(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
