# this should connect to the model DeepThought in models.py 

from django import forms
from .models import DeepThought

class DeepThoughtForm(forms.ModelForm):
	class Meta:
		model = DeepThought
		fields = "__all__"