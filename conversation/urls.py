from django.urls import path
from . import views

urlpatterns = [
    path('new-conversation/<int:item_pk>', views.new_conversation, name = "new_conversation"),
    path('inbox', views.inbox, name = "inbox"),
    path('conversation-detail/<int:pk>', views.conversation_detail, name = "conversation_detail"),
]