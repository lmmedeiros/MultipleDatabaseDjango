from django.db import models

from Profissao.models import Profissao

class Pessoa(models.Model):
   id = models.AutoField(primary_key = True)
   nome = models.CharField(max_length = 150)
   profissao = models.ForeignKey(
      Profissao, on_delete=models.CASCADE, blank=True, null=True
   )

   class Meta:
      app_label = 'Pessoa'
      db_table = 'pessoas'

   def __str__(self):
      return self.nome