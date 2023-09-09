from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils import timezone



# Create your models here.


class Qusetion(models.Model):
    author = models.ForeignKey(User, related_name='question_auther' , on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    content = models.TextField(max_length=30000)
    tag = TaggableManager()
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.question




class Answer(models.Model):
    author = models.ForeignKey(User , related_name='answer_auther' , on_delete=models.CASCADE)
    question = models.ForeignKey(Qusetion , related_name='n' , on_delete=models.CASCADE) 
    answer = models.TextField(max_length=40000)
    create_date= models.DateTimeField(default=timezone.now)

    
    def __str__(self):
        return self.answer


