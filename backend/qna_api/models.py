# 📌 Step 2: Build the Django Backend API
# 1️⃣ Create a Model for Q&A (Optional)
# If you want to store questions and answers in a database, create a simple model. If not, you can skip this.

from django.db import models
# Create your models here.

class QuestionAnswer(models.Model):
    question=models.TextField()
    answer=models.TextField()
    
    
    def __str__(self):
        return self.question
        
