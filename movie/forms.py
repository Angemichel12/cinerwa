from django import forms
from django.forms import ModelForm
from .models import Categories, Actor, Movies

class MoviesForm(ModelForm):
	class Meta:
		model = Movies
		fields = "__all__"

		labels = {
			'title': '',
			'release_date': '',
			'length': '',
			'movie_trailer_link': '',
			'poster': '',
			'actors': '',
			'views': '',
			'movie_categories': '',
			'movie_poster': '',
			'description': '',

		}

		widgets = {
			'title': forms.TextInput(attrs={'class':'form-contral'}),
			'release_date': forms.TextInput(attrs={'class':'form-contral'}),
			'length': forms.TextInput(attrs={'class':'form-contral'}),
			'movie_trailer_link': forms.TextInput(attrs={'class':'form-contral'}),
			'poster': forms.Select(attrs={'class':'form-select'}),
			'actors': forms.Select(attrs={'class':'form-select'}),
			'views': forms.TextInput(attrs={'class':'form-contral'}),
			'movie_categories': forms.Select(attrs={'class':'form-contral'}),
			'description': forms.Textarea(attrs={'class':'form-contral'}),

		}