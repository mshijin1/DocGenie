# 2️⃣ Create a Serializer for the Q&A Model (Optional)
# This will allow us to serialize data for easy API communication.

from rest_framework import serializers
from .models import QuestionAnswer

class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=QuestionAnswer
        fields=['question','answer']