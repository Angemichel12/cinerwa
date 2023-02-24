from django.urls import path
from .views import registration_page, profile, aboutuspage


urlpatterns = [
	path('register/', registration_page, name='register' ),
	path('profile/', profile, name='profile' ),
	path('about/', aboutuspage, name='about' ),
]
