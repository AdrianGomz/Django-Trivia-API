from rest_framework import viewsets
from .serializers import QuestionSerializer
from .models import Question


class QuestionsViewset(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
