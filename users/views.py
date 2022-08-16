from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def registration_page(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'{username}, Account is created. Login now!')
			return redirect('login')

	else:
		form = UserRegistrationForm()
	return render(request, 'register.html', {'form' : form})

@login_required
def profile(request):
	if request.method == 'POST':

		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		if u_form.is_valid() and p_form.is_valid():

			u_form.save()
			p_form.save()
			messages.success(request, f'Your Account have been updated')
			return redirect('profile')

	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {'u_form':u_form, 'p_form':p_form}
	return render(request, 'profile.html', context)

def aboutuspage(request):
	return render(request, 'aboutus.html')