from django.conf import settings
from django.db import models
from django.urls import reverse

class Trail(models.Model):
	title = models.CharField(max_length=255)
	about = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	distance = models.PositiveSmallIntegerField
	duration = models.TimeField
	difficulty = models.CharField(max_length=5)
	author = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
	)

	#image upload
	image = models.ImageField(upload_to='image/', default='imagelink')
	image_uploaded_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('trail_detail', args=[str(self.id)])

class Comment(models.Model):
	trail = models.ForeignKey(Trail, on_delete=models.CASCADE, related_name='comments')
	comment = models.CharField(max_length=140)
	author = models.ForeignKey(
			settings.AUTH_USER_MODEL,
			on_delete=models.CASCADE,
		)

	def __str__(self):
		return self.comment

	def get_absolute_url(self):
		return reverse('trail_list')

# 
# class Document(models.Model):
#     description = models.CharField(max_length=255, blank=True)
#     document = models.ImageField(upload_to='media/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)