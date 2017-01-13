from django.db import models

# Create your models here.
class Organizacao(models.Model):
	STATUS_CHOICES = (('A', 'active'),('I', 'inactive'))
	nome = models.CharField('Nome', max_length=100)
	codigo = models.CharField('Código', max_length=100, null=True)
	status = models.CharField('Status', max_length = 10, choices=STATUS_CHOICES)
	parent_id = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.nome
