from django.urls import path, reverse
from .views import (
	AuthorCreateView,
	AuthorDeleteView,
	AuthorDetailView, 
	AuthorListView, 
	AuthorUpdateView,
	HomeListView, 
	PublicationAuthorCreateView,
	PublicationCreateView,
	PublicationDetailView, 
	PublicationListView, 
	BookListView
)
from . import views 

urlpatterns = [ 
	#Below is how you assign routes for function-based views 
	path('', HomeListView.as_view(), name='mainapp-home'), 
	path('about/', views.about, name='about-page'),

	# Below, for class-based views
	# Use variables to specify a distinct route per author
	#The generic class-based detail view EXPECTS to be passed a parameter named pk. If you're writing your own function view you can use whatever parameter name you like, or indeed pass the information in an unnamed argument.
	path('authors/<slug:slug>/<int:pk>', AuthorDetailView.as_view(), name='author-detail-page'),
	path('authors/', AuthorListView.as_view(), name='authors-page'),
	path('authors/new/', AuthorCreateView.as_view(), name='authors-new-page'),
	path('authors/<slug:slug>/<int:pk>/update/', AuthorUpdateView.as_view(), name='author-update-page'),
	path('authors/<slug:slug>/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author-delete-page'),

	# path('authors/<first_name>_<slug:slug>/', views.AuthorDetailView.as_view(), name='author-detail-first-last'),
	# path('authors/<middle_name>_<slug:slug>/', views.AuthorDetailView.as_view(), name='author-detail-middle-last'),
	# path('authors/<first_name>_<middle_name>_<slug:slug>/', views.AuthorDetailView.as_view(), name='author-detail-first-middle-last'),
	path('publications/', PublicationListView.as_view(), name='publications-page'),
	path('publications/<slug:slug>/<int:pk>/', PublicationDetailView.as_view(), name='publication-detail-page'),
	path('publications/new/', PublicationCreateView.as_view(), name='publications-new-page'),
	path('publications/new/authors/', PublicationAuthorCreateView.as_view(), name='publication-authors-new-page'),
	path('books/', BookListView.as_view(), name='books-page'),
] 