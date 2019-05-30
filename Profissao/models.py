from django.db import models

class Profissao(models.Model):
   id = models.AutoField(primary_key = True)
   profissao = models.CharField(max_length = 100)

   class Meta:
      app_label = 'Profissao'
      db_table = 'profissoes'

   def __str__(self):
      return self.profissao