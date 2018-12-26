from django import forms
# from multi_email_field.forms import MultiEmailField
from .models import Sistem
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from datetime import datetime

class SistemForm(forms.ModelForm):
    
    # mula = forms.DateTimeField(widget=DateTimeInput())
    # akhir = forms.DateTimeField(widget=DateTimeInput())

    # # Verify Masa mula mestilah lebih awal daripada masa akhir
    # def clean(self):
    #     data = self.cleaned_data
    #     # print(str(self.cleaned_data['mula'])[:-9],self.cleaned_data['akhir'])
    #     if datetime.strptime(str(self.cleaned_data['mula'])[:-9],'%Y-%m-%d %H:%M') >= datetime.strptime(str(self.cleaned_data['akhir'])[:-9],'%Y-%m-%d %H:%M'):
    #         raise forms.ValidationError("Masa tarikh / masa mula mestilah lebih awal daripada tarikh / masa akhir !") 
    #     return data

    class Meta:
        model = Sistem
        fields = ('NamaSistem', 'Tahun', 'Status','PemilikSistem',)