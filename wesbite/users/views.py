from django.shortcuts import render
from .forms import RegisterForm


def register(request):

	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = RegisterForm()

	context = {'form': form}
	return render(request, 'users/register.html', context)