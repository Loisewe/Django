from .models import Genre,Album,Song
from django.shortcuts import render, get_object_or_404
# Create your views here.
def index(request) :
    all_albums=Album.objects.all()
    all_songs=Song.objects.all()
    context = {'all_albums':all_albums}

    return render(request, 'music/index.html',context)
    # html = ''
    # for album in all_albums:
    #     url='/music/'+ str(album.id)
    #     html += '<a href="' + url + '">' + str(album.genre_title) +'</a><br>'
def details(request, album_id):
    album = get_object_or_404(Album,pk = album_id)
    # try:
    #     album = Album.objects.get(pk=album_id)
    # except Album.DoesNotExist:
    #     raise  Http404("There no such album :((")
    return render(request,'music/detail.html',{'album':album})