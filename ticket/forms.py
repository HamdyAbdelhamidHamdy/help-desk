from django import forms
from .models import Ticket
from django.forms import FileInput


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['name', 'description', 'status', 'priority', 'image']

