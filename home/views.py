from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from .models import Category, Dish, Gallery
from .forms import ReservationForm


def index(request):
    categories = Category.objects.filter(is_visible=True).order_by('sort')
    gallery = Gallery.objects.filter(is_visible=True).order_by('created_at')
    book_table_form = ReservationForm()

    context = {
        'categories': categories,
        'gallery': gallery,
        'book_table_form': book_table_form
    }

    return render(request, 'index.html', context)
