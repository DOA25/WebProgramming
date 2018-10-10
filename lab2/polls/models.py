from django.db import models
import datetime
from django.utils import timezone

class question(models.Model): #Creates a new row in the question database
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)

class choice(models.Model): #Creates a new row in the choice database
    question = models.ForeignKey(question, on_delete=models.CASCADE) #creates a Foreign Key
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
