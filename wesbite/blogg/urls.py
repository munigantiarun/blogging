from django.urls import path
from .views import *

urlpatterns = [
	path('', HomeView.as_view(), name = 'blog-home'),
	path('entry/<int:pk>/', HomeDetail.as_view(), name='entry-detail'),
	path('blist/', BlogList.as_view(), name='blog-list'),
	path('ldetail/<int:pk>/', ListDetail.as_view(), name='list-detail'),
	path('create_entry/', CreateEntryView.as_view(success_url='/'), name='create-entry')
]