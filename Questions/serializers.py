from rest_framework import serializers
from .models import Question


class QuestionSerializer (serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Question
        fields = '__all__'
