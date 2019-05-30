from django.db import models

from Profissao.models import Profissao

class Pessoa(models.Model):
   id = models.AutoField(primary_key = True)
   nome = models.CharField(max_length = 100)

   class Meta:
      app_label = 'Pessoa'
      db_table = 'pessoas'

   def __str__(self):
      return self.nome