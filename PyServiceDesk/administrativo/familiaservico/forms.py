from django import forms
from .models import FamiliaServico
from PyServiceDesk.administrativo.organizacao.models import Organizacao

class FamilyServiceForm(forms.ModelForm):
	class Meta:
		model = FamiliaServico
		fields = ['nome', 'descricao', 'status', 'org_id']
		widgets = {
			'descricao': forms.Textarea(attrs={'cols': 40, 'rows': 10, 'class': 'form-control'}),
		}
		labels ={
			'descricao': 'Descrição',
		}
	STATUS_CHOICES = (
		('P', 'Produção'),
		('I', 'Implementação'),
		('O', 'Obsoleto')
	)
	nome = forms.CharField(max_length=100, label='Nome')
	status = forms.ChoiceField(choices=STATUS_CHOICES, required=False)
	org_id = forms.ModelChoiceField(queryset=Organizacao.objects.filter(status='A'), required=True, empty_label="Nenhum", label="Organização")
