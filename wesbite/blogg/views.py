from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.
from .models import Entry
from django.http import JsonResponse



class HomeView(ListView):
	model = Entry
	template_name = 'blogg/index.html'
	context_object_name = "entries"
	ordering = ['-entry_date']
	paginate_by = 4

class HomeDetail(DetailView):
	model = Entry
	template_name = 'blogg/entry_detail.html'

class BlogList(ListView):
	model = Entry
	template_name = 'blogg/blog_list.html'
	context_object_name = "entries"
	ordering = ['-entry_date']
	paginate_by = 15

class ListDetail(DetailView):
	model = Entry
	template_name = 'blogg/list-detail.html'

class CreateEntryView(CreateView):
	model = Entry
	template_name = 'blogg/create-entry.html'
	fields = ['entry_title', 'entry_text']

	def form_valid(self, form):
		form.instance.entry_author = self.request.user
		return super().form_valid(form)
