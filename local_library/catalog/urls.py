from django.urls import path
from django.conf.urls import url
from catalog import views
# from django.contrib.auth.views import LoginView

app_name = 'catalog'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('books',views.BookListView.as_view(),name='books_list'),
    path('book/<int:pk>',views.BookDetailView.as_view(),name='book_detail'),
    path('author/<int:pk>',views.AuthorDetailView.as_view(),name='author_detail'),
    path('authors',views.AuthorListView.as_view(),name='author_list'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout',views.LogoutView.as_view(),name='logout'),
]