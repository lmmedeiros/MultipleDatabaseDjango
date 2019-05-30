from django.shortcuts import render

from .models import Pessoa
from .forms import PessoaForm

def pessoa(request):
   form = PessoaForm(request.POST or None)
   listagem = Pessoa.objects.using('pessoas_db').all()

   if request.method == 'POST':
      if form.is_valid():
         form.save()

   params = {
      'form': form,
      'listagem': listagem
   }
   return render(request, 'pessoa.html', params)
