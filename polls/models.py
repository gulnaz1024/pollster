from django.db import models
from django.core.files import File
import sys

class Question(models.Model):
    question_text = models.FilePathField(path='documents/')
    #question_text = models.FileField(upload_to='documents/') #
    pub_date = models.DateTimeField('date published')


    def __str__(self):
        data_file = open('documents/1.txt' , 'r')
        data = data_file.read()
        return data #str(self.question_text)
    
   
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


