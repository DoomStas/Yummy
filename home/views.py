from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from .models import Category, Dish
#from django.db.models import Count
# Create your views here.
def index(request):

    categories = Category.objects.filter(is_visible=True).order_by('sort')
    context = {'categories': categories}
    return render(request, 'index.html', context)