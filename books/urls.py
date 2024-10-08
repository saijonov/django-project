from django.urls import path
from .views import BookListApiView, BookDetailApiView, \
    BookUpdateApiView, BookDeleteApiView, BookCreateApiView, \
    BookListCreateApiView, BookUpdateDeleteView

urlpatterns = [
    path('books/', BookListApiView.as_view()),
    path('booklistcreate/', BookListCreateApiView.as_view()),
    path('bookupdatedelete/<int:pk>', BookUpdateDeleteView.as_view()),
    path('books/create/', BookCreateApiView.as_view()),
    path('books/<int:pk>/', BookDetailApiView.as_view()),
    path('books/<int:pk>/delete/', BookDeleteApiView.as_view()),
    path('books/<int:pk>/update/', BookUpdateApiView.as_view()),

]
