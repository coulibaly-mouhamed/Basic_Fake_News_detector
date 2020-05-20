from django.db import models

# Create your models here.
  #Thanks to this class we will have access to the news
class news_url(models.Model):
	news_url =models.CharField(max_length=300)
	score = models.IntegerField(default=0) #we will stock here the news score
 	
#Represents ouput of our algorithm(score)



 	