from django import forms
from .models import Message

class SendMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['nom', 'post_nom', 'email', 'telephone', 'message']