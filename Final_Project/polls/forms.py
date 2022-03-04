from django.forms import ModelForm
from .models import ImageCloud


class ImageForm(ModelForm):
    class Meta:
        model = ImageCloud
        fields = ['image']
