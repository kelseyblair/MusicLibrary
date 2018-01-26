from django.db import models

class Song(models.Model):
	song_name = models.CharField(max_length=200)
	artist_name = models.CharField(max_length=200)
	album_name = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return self.song_name

	