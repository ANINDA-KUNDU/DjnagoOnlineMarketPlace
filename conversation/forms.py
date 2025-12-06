from django import forms
from .models import ConversationMessage


class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        widgets = {
            'content': forms.TextInput(attrs={
                'class': 'mango',
                'placeholder': 'Type your message ...',
            }),
        }
        labels = {
            'content': '',
        }