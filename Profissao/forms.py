from django import forms

from .models import Profissao

class ProfissaoForm(forms.ModelForm):
   profissao = forms.CharField(widget=forms.TextInput())

   class Meta:
      model = Profissao
      fields = '__all__'