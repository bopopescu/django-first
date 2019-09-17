from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Book,BookInstance,Author,Language,Genre
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
# Create your views here.

class IndexView(LoginRequiredMixin,TemplateView):
    login_url = '/login'
    template_name = 'index.html'
    # num_visit = 0

    def get(self,request,*args,**kwargs):       
        self.num_visit = request.session.get('num_visit',0)
        self.num_visit += 1
        request.session['num_visit'] = self.num_visit
        context = self.get_context_data()
        return self.render_to_response(context)
    
    
    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['books'] = Book.objects.all().count()
         context['book_instance'] = BookInstance.objects.all().count()
         context['available'] = BookInstance.objects.filter(status__exact='a').count()
         context['author'] = Author.objects.all().count()
         context['num_visit'] = self.num_visit
         context['last_login'] = User.objects.get(pk__exact=self.request.session['id']).last_login
         return context


class BookListView(LoginRequiredMixin,ListView):
    login_url = '/login'
    model = Book
    template_name = 'book_list.html'
    # context_object_name = 'book'


class BookDetailView(LoginRequiredMixin,DetailView):
    login_url = '/login'
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book_detail'

    
    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['instances'] = BookInstance.objects.filter(book__id=self.kwargs['pk']) 
         print(context['instances'])
         return context
     

class AuthorListView(LoginRequiredMixin,ListView):
    login_url = '/login'
    model = Author
    template_name = 'author_list.html'
    context_object_name = 'list'

class AuthorDetailView(LoginRequiredMixin,DetailView):
    login_url = '/login'
    model = Author
    template_name = 'author_detail.html'
    context_object_name = 'author'