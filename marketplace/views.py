from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from marketplace.models import Item, Category
from marketplace.forms import AddItemForm, EditAddItemForm
from django.contrib import messages
from django.db.models import Q
# Create your views here.

def detail_item(request, pk):
    details = get_object_or_404(Item, id = pk)
    related_items = Item.objects.filter(is_sold = False).exclude(pk = pk)
    return render(request, 'marketplace/detail_item.html', {'details': details, 'related_items': related_items})

def add_item(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            messages.success(request, 'Your Item has been created successfully.')
            return redirect('home')
    else:
        form = AddItemForm()
    return render(request, 'marketplace/add_item.html',{'form': form})

def edit_add_item(request, pk):
    items = get_object_or_404(Item, id = pk, created_by = request.user)
    if request.method ==  'POST':
        form = EditAddItemForm(request.POST, request.FILES, instance = items)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item updated successfully.')
            return redirect('detail_item',pk=items.id)
    else:
        form = EditAddItemForm(instance = items)
    return render(request, 'marketplace/edit_add_item.html', {'form': form})

def delete_item(request, pk):
    items = get_object_or_404(Item, id = pk, created_by = request.user)
    items.delete()
    messages.success(request, 'Your item has been successfully deleted.')
    return redirect('home')

def search(request):
    query = request.GET.get('query', '')
    items = Item.objects.none()
    if query:
        items = Item.objects.filter(Q(name__icontains = query) | Q(description__icontains = query))
    
    categories = Category.objects.all()
    category_id = request.GET.get('category', 0)
    if category_id:
        items = Item.objects.filter(category_id = category_id)
    return render(request, 'marketplace/search.html', {'query': query, 'items': items, 'categories': categories, 'category_id': category_id})