from django.contrib import admin

# Register your models here.

from .models import Books, Category, Tag, BookAuthor

admin.site.register([Books, Category, Tag, BookAuthor])
