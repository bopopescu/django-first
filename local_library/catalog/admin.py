from django.contrib import admin
from .models import Book, BookInstance, Author, Genre, Language, LibraryUser
# Register your models here.

# @admin.register(Members) 
# class MemberAdmin(admin.ModelAdmin):
#     list_display = ('username', 'password', 'last_login', 'no_visits')


@admin.register(Author) 
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'author', 'display_genre')


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'due_back', 'status', 'id')
    list_filter = ('status', 'due_back')                    #to filter out the listed result

@admin.register(LibraryUser)
class LibraryUserAdmin(admin.ModelAdmin):
    pass

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass






