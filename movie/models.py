from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Categories(models.Model):
	name = models.CharField(max_length=50, default="Action")

	def __str__(self):
		return self.name

class Movies(models.Model):
	title = models.CharField(max_length=150)
	release_date =models.DateField(default=timezone.now)
	length = models.CharField(max_length=4, default='60')
	movie_trailer_link = models.URLField(max_length = 200)
	poster = models.ForeignKey(User, on_delete=models.CASCADE)
	views = models.IntegerField(default=0)
	movie_categories = models.ForeignKey(Categories,on_delete=models.CASCADE,default=1)
	favourites = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)
	movie_poster = models.ImageField(upload_to='movies/')
	description = models.TextField()


	class Meta:
		ordering =("-release_date",)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
	    return reverse('movies_detail', kwargs={'pk': self.pk})
	

		