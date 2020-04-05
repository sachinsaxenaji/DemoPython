from django.db import models

# Create your models here.
class Destination(models.Model):
	
	name = models.CharField(max_length=100)
	img= models.ImageField(upload_to = 'pics')
	desc= models.TextField()
	price= models.IntegerField()
	offer= models.BooleanField(default = False)

class News(models.Model):
	
	title = models.CharField(max_length=100)
	category = models.CharField(max_length=100)
	date = models.CharField(max_length=100)
	month= models.CharField(max_length=10)
	image= models.ImageField(upload_to = 'pics')
	post_text= models.TextField()
	trending= models.BooleanField(default = False)

class New:

	title: str
		
	