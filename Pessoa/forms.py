from django import forms

from .models import Pessoa
from Profissao.models import Profissao

class PessoaForm(forms.ModelForm):
   nome = forms.CharField(required = True, widget=forms.TextInput())
   profissao = forms.ModelChoiceField(required = True, queryset=Profissao.objects.using('profissoes_db').all(),\
      empty_label='Selecione uma profissao...', \
   )

   class Meta:
      model = Pessoa
      fields = '__all__'