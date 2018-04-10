from django.db import models

# Create your models here.
class Artist (models.Model):
    artist_name = models.CharField(max_length=100)
    def __str__(self):
        return self.artist_name

class Genre(models.Model):
    genre_title = models.CharField(max_length=50)
    def __str__(self):
        return self.genre_title

class Album (models.Model):
    releasedate = models.DateTimeField()
    album_title = models.CharField(max_length=250)
    album_logo = models.CharField(max_length=1000)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
    studio = models.CharField(max_length=100)
    def __str__(self):
        return self.album_title
class Song (models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type= models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    def __str__(self):
        return self.song_title

