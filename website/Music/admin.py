from django.contrib import admin
from .models import Album,Song,Artist,Genre

admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(Genre)
# Register your models here.
