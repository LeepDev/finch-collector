# forms.py

from django.forms import ModelForm
from .models import Bathing

class BathingForm(ModelForm):
  class Meta:
    model = Bathing
    fields = ['date', 'bath']