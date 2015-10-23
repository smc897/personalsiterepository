import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
	    return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
	    return self.choice_text


####user information for contact page        
class userinfo(models.Model):
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    def __unicode__(self):
        return self.name+' '+self.phone+' '+self.email
        
###about information
class about(models.Model):
    path=models.CharField(max_length=200)
    description=models.CharField(max_length=2000)
    def __unicode__(self):
        return self.path+' '+self.description
        
###project information
class project(models.Model):
    path=models.CharField(max_length=200)
    description=models.TextField()
    def __unicode__(self):
        return self.path+' '+self.description
            
		