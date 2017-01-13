from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404, JsonResponse
from django.core import serializers
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Organizacao
from .forms import OrganizacaoForm
from django.db.models import Q

# Create your views here.
@login_required(login_url='web:login')
def organization(request):
	if request.method == 'GET':
		organization_list = Organizacao.objects.all()
		return render(request, 'organizacoes.html', {'organization_list': organization_list})
	else:
		q = Q()
		if request.POST['nome'] != "":
			nome = str(request.POST['nome'])
			q = q & Q(nome__contains = nome)
		if request.POST['code'] != "":
			code = request.POST['code']
			q = q & Q(codigo__contains = code)
		if request.POST['status'] != "":
			status = request.POST['status']
			q = q & Q(status = status)
		organization_list = Organizacao.objects.filter(q)
		return render(request, 'organizacoes.html', {'organization_list': organization_list})
@login_required(login_url='web:login')
def new_organization(request):
	if request.method == 'POST':
		form = OrganizacaoForm(request.POST)
		if form.is_valid():
			org = Organizacao()
			org.nome = request.POST['nome']
			org.codigo = request.POST['codigo']
			org.status = request.POST['status']
			if request.POST['parent_id'] != '':
				org.parent_id = Organizacao.objects.get(pk=request.POST['parent_id'])
			org.save()
			return redirect('administrativo:organizacao:detail_organization', pk=org.pk)
	else :
		form = OrganizacaoForm()

	return render(request, 'new_organization.html', {'form': form})
@login_required(login_url='web:login')
def detail_organization(request, pk):
	organization = get_object_or_404(Organizacao, pk=pk)
	if organization is not None:
		return render(request, 'detail_organization.html', {'organization':organization})
	else :
		raise Http404("No Organizacao found")
@login_required(login_url='web:login')
def edit_organization(request, pk):
	organization = get_object_or_404(Organizacao, pk=pk)
	if organization is not None:
		if request.method == 'POST':
			form = OrganizacaoForm(request.POST, instance=organization)
			if form.is_valid():
				organization.nome = request.POST['nome']
				organization.codigo = request.POST['codigo']
				organization.status = request.POST['status']
				if request.POST['parent_id'] != '':
					organization.parent_id = Organizacao.objects.get(pk=request.POST['parent_id'])
				organization.save()
				return redirect('administrativo:organizacao:detail_organization', pk=organization.pk)
		else :
			form = OrganizacaoForm(instance=organization)
			return render(request, 'edit_organization.html', {'form': form, 'pk': organization.pk})
	else :
		raise Http404("No Organizacao found")
