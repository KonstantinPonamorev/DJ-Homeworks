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
    # books_objects = Book.objects.order_by('pub_date')
    # paginator = Paginator(books_objects, 5)
    # page = paginator.get_page(1)
    context = {
        'books': books_objects
    }
    return render(request, template, context)

