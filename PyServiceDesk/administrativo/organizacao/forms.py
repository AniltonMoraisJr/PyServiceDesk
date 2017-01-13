from django import forms
from .models import Organizacao

class OrganizacaoForm(forms.ModelForm):
	class Meta:
		model = Organizacao
		fields = ['nome', 'codigo', 'status', 'parent_id']
	STATUS_CHOICES = (
		('A', 'Ativo'),
		('I', 'Inativo')
	)
	nome = forms.CharField(max_length=100, label='Nome')
	codigo = forms.CharField(max_length=100, required=False, label='Código')
	status = forms.ChoiceField(choices=STATUS_CHOICES, required=False)
	parent_id = forms.ModelChoiceField(queryset=Organizacao.objects.all(), required=False, empty_label="Nenhum", label="Matriz")
