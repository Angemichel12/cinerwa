from django.shortcuts import render,redirect, get_object_or_404

from .models import Movies, Categories
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
	context = {
		'movies':Movies.objects.all()
    }
	return render(request, 'index.html', context)


class MovieListView(ListView):

	model = Movies
	template_name = 'index.html'
	context_object_name = 'movies'
	ordering = ['-release_date'] 
	paginate_by = 3



class MovieDetailView(DetailView):

	model = Movies
	template_name = 'movie_details.html'

class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movies
    fields = ['title', 'release_date', 'length', 'movie_trailer_link', 'movie_categories', 'movie_poster', 'description']
    template_name = 'add_movies.html'

    def form_valid(self, form):
        form.instance.poster = self.request.user
        return super().form_valid(form)

class MovieUpdateView(UpdateView):
	model = Movies
	fields = ['title', 'release_date', 'length', 'movie_trailer_link', 'movie_categories', 'movie_poster', 'description']
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
    success_url = 'home'

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





