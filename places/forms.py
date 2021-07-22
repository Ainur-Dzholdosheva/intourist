from django import forms
from .models import Place, FeedBack

class PlaceForm(forms.ModelForm):
    class Meta:
        model=Place
        fields = ['name', 'location', 'description']

class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ('place', 'text')
