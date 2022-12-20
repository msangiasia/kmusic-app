from django.db import models

# Create your models here.

class User(models.Model):
	user_id =models.IntegerField(default=0)
	name = models.CharField(max_length= 100)
	username = models.CharField(max_length=100)
	user_email = models.EmailField()

	def __str__(self):
		return self.name

class Artist(models.Model):
	art_name = models.CharField(max_length= 100)
	art_username = models.CharField(max_length= 100)
	art_type_list = [
	('R&B', "RAPPER"),
	('JZ', 'JAZZ'),
	('HIPHOP', 'HIPPOP')
	]
	art_type = models.CharField(max_length=6, choices=art_type_list)


	def __str__(self):
		return self.cat_name


class Song(models.Model):
	id = models.BigAutoField(primary_key=True)
	artist = models.ForeignKey(Artist, on_delete = models.CASCADE)
	date = models.DateField()
	song_name = models.CharField(max_length=100)
	song_type = models.CharField(max_length=100)
	recorded_studio = models.CharField(max_length=100)
	song_file = models.FileField(upload_to="songs")


	def __str__(self):
		return self.song_name

class Album(models.Model):
	album_id = models.IntegerField()
	album_name = models.CharField(max_length=100)
	album_song = models.ForeignKey(Song, on_delete= models.CASCADE)
