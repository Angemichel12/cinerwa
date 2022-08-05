from django.urls import path
from .views import registration_page, profile


urlpatterns = [
	path('register/', registration_page, name='register' ),
	path('profile/', profile, name='profile' ),
]