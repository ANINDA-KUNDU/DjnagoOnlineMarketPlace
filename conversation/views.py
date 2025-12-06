from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Conversation, ConversationMessage
from .forms import ConversationMessageForm
from marketplace.models import Item
# Create your views here.
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    
    if item.created_by == request.user:
        return redirect('dashboard')

    conversations = Conversation.objects.filter(members__in=[request.user.id])
    
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        
        if form.is_valid():
            conversation = Conversation.objects.create( item = item )
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()
            
            conversation_message = form.save( commit = False )
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            return redirect('detail_item', pk=item_pk)
    else:
        form = ConversationMessageForm()
    return render(request, 'conversation/new_conversation.html', {'form': form})

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id]).prefetch_related('members', 'item')
    return render(request, 'conversation/inbox.html', {'conversations': conversations})


@login_required
def conversation_detail(request, pk):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).prefetch_related('messages', 'messages__created_by').get(pk=pk)
    
    if request.method == "POST":
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation_message = form.save( commit =  False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            conversation.save()
            return redirect('conversation_detail', pk=pk)
    else:
        form = ConversationMessageForm()
    return render(request, 'conversation/conversation_detail.html', {'conversation': conversation, 'form': form})