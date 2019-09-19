from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, View
from .models import Book,BookInstance,Author,Language,Genre, LibraryUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate    
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime
# Create your views here.

class IndexView(LoginRequiredMixin,TemplateView):
    login_url = '/login'
    template_name = 'index.html'
 
    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['books'] = Book.objects.all().count()
         context['book_instance'] = BookInstance.objects.all().count()
         context['available'] = BookInstance.objects.filter(status__exact='a').count()
         context['author'] = Author.objects.all().count()
         context['num_visit'] = (LibraryUser.objects.get(user_id=self.request.user.id)).no_visits
         context['last_login'] = LibraryUser.objects.get(user_id=self.request.user.id).last_login
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


class LogoutView(LoginRequiredMixin,View):

    def get(self,request):
        u = LibraryUser.objects.get(user_id=request.user.id)
        u.last_login = datetime.now()
        u.save()
        # request.user.last_login = datetime.now()
        print(u.last_login)
        # request.user.save()
        response = logout(request)
        return HttpResponseRedirect(reverse('catalog:index'))


class LoginView(View):
    model = LibraryUser

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username=username,password=password)

        if user :
            u = LibraryUser.objects.get(user_id=user.id)    #(user_id=request.user.pk) -> not working
            u.no_visits += 1
            u.save()
            login(request,user)
            return HttpResponseRedirect(reverse('catalog:index'))
        else :
            return HttpResponseRedirect(reverse('catalog:login'))
    
    def get(self,request):
        return render(request,'registration/login.html')

        

        