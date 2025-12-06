from django import forms
from .models import Item

class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'image', 'category', 'price', 'description',)
        

class EditAddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = Itemfields = ('name', 'image', 'category', 'price', 'description','is_sold',)