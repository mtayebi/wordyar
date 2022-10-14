from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from exams import models


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model: models.Question
        fields = ['question', 'answer']
    
    
