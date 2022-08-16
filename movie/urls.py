from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import(homepage, 
	MovieListView, 
	MovieDetailView, 
	MovieCreateView,
	MovieUpdateView,
	MovieDeleteView,
	favourite_add,
	movie_favourite_list,
	search_movie,
	
	) 



urlpatterns = [
	path('', MovieListView.as_view(), name='home'),
	path('add_movie/', MovieCreateView.as_view(), name='add_movie'),
	path('movies_detail/<int:pk>/', MovieDetailView.as_view(), name='movies_detail'),
	path('movies_detail/<int:pk>/update/', MovieUpdateView.as_view(), name='movie_update'),
	path('movies_detail/<int:pk>/delete/', MovieDeleteView.as_view(), name='movie_delete'),
	path('fav/<int:id>', favourite_add, name='favourite_add'),
	path('favourite/', movie_favourite_list, name='favourite_list'),
	path('search_movie', search_movie, name='search-movie'),

	]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)