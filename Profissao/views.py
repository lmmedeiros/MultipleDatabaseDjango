from django.shortcuts import render

from .forms import ProfissaoForm
from .models import Profissao

def profissao(request):
   form = ProfissaoForm(request.POST or None)
   listagem = Profissao.objects.using('profissoes_db').all()

   if request.method == 'POST':
      if form.is_valid():
         form.save()

   params = {
      'form': form,
      'listagem': listagem
   }

   return render(request, 'profissao.html', params)
