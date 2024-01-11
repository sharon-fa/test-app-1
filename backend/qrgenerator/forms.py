from django import forms
from .models import QRCodeData

# class QRCodeForm(forms.ModelForm):
#     class Meta:
#         model = QRCodeData
#         fields = ['data_text']

class QRCodeForm(forms.Form):
    client_name = forms.CharField(label='Client', max_length=100)
    service_provider = forms.CharField(label='Service Provider', max_length=100)
    job_id = forms.CharField(label='Job ID', max_length=100)