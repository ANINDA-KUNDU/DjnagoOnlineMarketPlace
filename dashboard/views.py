from django.shortcuts import render, get_object_or_404
from marketplace.models import Category, Item
# Create your views here.

def dashboard(request):
    items = Item.objects.filter( created_by = request.user )
    return render(request, 'dashboard/dashboard.html',{'items': items})