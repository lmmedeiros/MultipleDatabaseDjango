from django.shortcuts import render

from .forms import ProfissaoForm, SearchForm
from .models import Profissao

def profissao(request):
   form = ProfissaoForm(request.POST or None)
   listagem = Profissao.objects.using('profissoes_db').all()
   search = SearchForm(request.POST or None)

   if request.method == 'POST':
      if form.is_valid():
         form.save()

   busca = request.GET.get('search')
   if busca:
      listagem = Profissao.objects.using('profissoes_db').filter(profissao__icontains=busca)

   params = {
      'form': form,
      'listagem': listagem,
      'search': search,
   }

   return render(request, 'profissao.html', params)
