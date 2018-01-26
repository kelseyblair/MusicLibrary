from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Song
from .forms import NewSongForm


# Helper list to handle sorting by ascending or descending (see list())
headers = {'song_name' : 'asc',
		'artist_name' : 'asc',
		'album_name' : 'asc',}

# Index provides links to the other functions of the website. Redirects to search view.
def index(request):
	return redirect('/search')

#  Search provides a search box to search for items in the database. Shows results when search performed
def search(request):
	query = None
	return render(request, 'musiclibrary/search.html')

# Search for items in the list, return items that are exact matches in any field to the query
def searchresults(request, pk):
	# Get the 'q' parameter from the url
	query = request.GET.get('q')
	if query:
		# Results only matches exact phrase
		results = Song.objects.filter(Q(song_name=query) | Q(artist_name=query) | Q(album_name=query))
		return render(request, 'musiclibrary/search.html', {'results' : results, 'query' : query})
	# else search was pressed without entering anything
	else:
		results = None
		messages.error(request, 'Please enter a valid search')
	return render(request, 'musiclibrary/search.html')


# Addsong provides a form which to add a new item to the database
def addsong(request):
	if request.method == "POST":
		form = NewSongForm(request.POST)
		if form.is_valid():
			# Check for duplicate TODO.
			form.save()
			messages.success(request, 'Successfully added song!')
			return HttpResponseRedirect(request.path)
	else:
		form = NewSongForm()
	return render(request, 'musiclibrary/addsong.html', {'form' : form})


# List provides a list view of all items in the database
def list(request):	
	sort = request.GET.get('sort')
	songs = Song.objects.all()

	# handle sorting the list
	if sort:
		songs = songs.order_by(Lower(sort))
		if headers[sort] == "des":
			songs = songs.reverse()
			headers[sort] = "asc"
		else:
			headers[sort] = "des"

	# delete items that were checked
	if request.method == "POST":
		delete_list = request.POST.getlist('delete')
		delete_songs = songs.filter(id__in=delete_list)
		Song.objects.filter(id__in=delete_list).delete()

	return render(request, 'musiclibrary/list.html', {'songs' : songs})



