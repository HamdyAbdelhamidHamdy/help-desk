from django.core.exceptions import ValidationError

from .models import Ticket
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

MAX_SIZE = 10 * 1024 * 1024

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class FileFieldForm(forms.Form):
    file_field = MultipleFileField()


class TicketForm(forms.ModelForm):
    image = MultipleFileField(required=False)

    def clean_image(self):
        images = self.cleaned_data.get('image')
        if images:
            for img in images:
                if img.size > MAX_SIZE:
                    raise ValidationError(
                        _('The maximum file size that can be uploaded is %(size)s MB.'),
                        params={'size': MAX_SIZE / (1024 * 1024)},
                    )
        return images
    class Meta:
        model = Ticket
        fields = ['name', 'email','description', 'image','category']

