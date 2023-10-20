from qrapp.models import qr
from django import forms

class qrform(forms.ModelForm):
    class Meta:
     model = qr
     fields = ["name", "text"]
     