from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=200)
	image = models.CharField(max_length=500)
	time_taken = models.FloatField()
	ingredients = models.TextField()
	text = models.TextField()
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
