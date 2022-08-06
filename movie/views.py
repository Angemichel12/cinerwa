from django.shortcuts import render,redirect, get_object_or_404

from .models import Movies, Categories
from .forms import MoviesForm
from django.http import HttpResponseRedirect


from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import(
	ListView, 
	DetailView,
 	CreateView,
 	UpdateView,
 	DeleteView,
 	)
def search_movie(request):
	if request.method == "POST":
		searched = request.POST['searched']
		movies = Movies.objects.filter(title__contains = searched)

		return render(request, 'search_movie.html', {'movies':movies})
	else:
		return render(request, 'search_movie.html', {'searched':searched})


def favourite_add(request, id):
	movie = get_object_or_404(Movies, pk=id)
	if movie.favourites.filter(id=request.user.id).exists():
		movie.favourites.remove(request.user)

	else:
		movie.favourites.add(request.user)
	return HttpResponseRedirect(request.META['HTTP_REFERER'])

def homepage(request):
	return render(request, 'index.html')

def movies_list(request):

	context = {
        'categories': Categories.objects.all(),
		'movies':Movies.objects.all()
    }
	return render(request, 'home.html', context)

class MovieListView(LoginRequiredMixin, ListView):

	model = Movies
	template_name = 'movies_list.html'
	context_object_name = 'movies'
	ordering = ['-release_date'] 



class MovieDetailView(DetailView):

	model = Movies
	template_name = 'movie_details.html'

class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movies
    fields = ['title', 'release_date', 'length', 'movie_trailer_link', 'actors', 'movie_categories', 'movie_poster', 'description']
    template_name = 'add_movies.html'

    def form_valid(self, form):
        form.instance.poster = self.request.user
        return super().form_valid(form)

class MovieUpdateView(UpdateView):
	model = Movies
	fields = ['title', 'release_date', 'length', 'movie_trailer_link', 'actors', 'movie_categories', 'movie_poster', 'description']
	template_name = 'post_form.html'

	def form_valid(self, form):
	    form.instance.poster = self.request.user
	    return super().form_valid(form)

	def test_func(self):
	    movie= self.get_object()
	    if self.request.user == movie.poster:
	        return True

class MovieDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Movies
    template_name = 'movie_confirm_delete.html'
    success_url = ''

    def test_func(self):
        movie = self.get_object()
        if self.request.user == movie.poster:
            return True
        return False


def movie_favourite_list(request):
	user = request.user
	favourites_movies = user.favourites.all()
	context = {
		'favourites_movies':favourites_movies

	}
	return render(request, 'favourite.html', context)





