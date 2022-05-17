from django.core.paginator import Paginator
from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books_objects = Book.objects.order_by('pub_date')
    context = {
        'books': books_objects
    }
    return render(request, template, context)



def books_pub_date(request, pub_date):
    template = 'books/books_list.html'
    books_objects = Book.objects.filter(pub_date=pub_date)
    books_next = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()
    books_previous = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date').first()
    context = {
        'books': books_objects,
        'next_book': books_next,
        'previous_book': books_previous,
    }
    return render(request, template, context)

