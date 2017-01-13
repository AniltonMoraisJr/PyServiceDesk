from django.db import models
from PyServiceDesk.administrativo.organizacao.models import Organizacao

# Create your models here.
class FamiliaServico(models.Model):
	STATUS_CHOICES = (
		('P', 'Em Produção'),
		('I', 'Em Implementação'),
		('O', 'Obsoleto')
	)
	nome = models.CharField('Nome',max_length=100)
	org_id = models.ForeignKey(Organizacao, on_delete=models.SET_NULL, null=True)
	descricao = models.TextField('Descricao', null=True)
	status = models.CharField('Status', max_length=15, choices=STATUS_CHOICES)
	def __str__(self):
		return self.nome
