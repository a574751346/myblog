from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from mdeditor.fields import MDTextField

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=20)
	
	def __str__(self):
		return self.name
	
class Tag(models.Model):
	name = models.CharField(max_length=20)
	
	def __str__(self):
		return self.name

class Article(models.Model):
	title = models.CharField(max_length=50)
	intro = models.CharField(max_length=100, blank=True)
	#body = models.TextField()
	body = MDTextField()
	created_time = models.DateTimeField()
	modified_time = models.DateTimeField()
	numsay = models.IntegerField(default=0)
	numread = models.IntegerField(default=0)
	
	category = models.ForeignKey(Category)
	tags = models.ManyToManyField(Tag, blank=True)
	
	author = models.ForeignKey(User)
	
	def __str__(self):
		return self.title
		
	def get_absolute_url(self):
		return reverse('blog:detail', kwargs={'post_id':self.id})
	
	def increase_numread(self):
		self.numread+=1
		self.save(update_fields=['numread'])
		
class ExampleModel(models.Model):
	name = models.CharField(max_length=10)
	content = MDTextField()
