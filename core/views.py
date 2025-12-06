from django.shortcuts import render, get_object_or_404
from marketplace.models import Category, Item
# Create your views here.

def home(request):
    items = Item.objects.filter( is_sold = False )
    categories = Category.objects.all()
    return render(request, 'core/home.html', {
        'items': items,
        'categories': categories,
    })