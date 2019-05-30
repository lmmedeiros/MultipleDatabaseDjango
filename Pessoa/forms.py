from django import forms

from .models import Pessoa
from Profissao.models import Profissao

class PessoaForm(forms.ModelForm):
   nome = forms.CharField(widget=forms.TextInput())

   class Meta:
      model = Pessoa
      fields = '__all__'