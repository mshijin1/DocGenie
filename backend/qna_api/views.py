# 3️⃣ Set Up the Views (API Logic)
# Now we need to create the API logic that will call the pre-trained model (like BERT) to answer questions.

from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from transformers import pipeline

# Load the pre-trained model for Question-Answering
qa_model=pipeline("question-answering")

class QuestionAnswerView(APIView):
    def post(self,request):
        question=request.data.get('question')
        context=request.data.get('context') # pass the document or text
        
        # Answer the question using the model
        answer=qa_model({
            'question':question,
            'context':context
        })

        # Return the answer
        return Response({"answer": answer['answer']})