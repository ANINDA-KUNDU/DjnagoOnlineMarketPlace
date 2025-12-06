from django.urls import path
from . import views

urlpatterns = [
    path('deatil-item/<int:pk>', views.detail_item, name = "detail_item"),
    path('add-item', views.add_item, name = "add_item"),
    path('edit-add-item/<int:pk>', views.edit_add_item, name = "edit_add_item"),
    path('delete-item/<int:pk>', views.delete_item, name = "delete_item"),
    path('search', views.search, name = "search"),
]