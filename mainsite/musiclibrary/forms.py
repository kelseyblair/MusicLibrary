from django import forms
from .models import Song

# Form to add a new song to the database. ModelForms use the HTML <imput> elements
class NewSongForm(forms.ModelForm):
	# song_name = forms.CharField(max_length=200)
	# artist_name = forms.CharField(max_length=200)
	# album_name = forms.CharField(max_length=200) #This is not required

	class Meta:
		model = Song
		fields = ('song_name', 'artist_name', 'album_name')

	# form = NewSongForm()

	# newsong = Song.objects.get(pk=1)
	# form = NewSongForm(instance=newsong)

# Form to search for a song in the database
# class SearchForm(forms.ModelForm):

# Form to delete a song or many songs from the database
# class DeleteForm(forms.Form):

