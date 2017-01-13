from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404, JsonResponse
from django.core import serializers
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from PyServiceDesk.administrativo.organizacao.models import Organizacao
from .models import FamiliaServico
from .forms import FamilyServiceForm
from django.db.models import Q


# Create your views here.
#Family Service views
@login_required(login_url='web:login')
def familyservice(request):
	if request.method == 'GET':
		familyservice_list = FamiliaServico.objects.all()
		return render(request, 'familyservices.html', {'familyservice_list': familyservice_list})
	else:
		q = Q()
		if request.POST['name'] != "":
			name = str(request.POST['name'])
			q = q & Q(nome__contains = name)
		if request.POST['description'] != "":
			description = request.POST['description']
			q = q & Q(descricao__contains = description)
		if request.POST['status   '] != "":
			status = request.POST['status']
			q = q & Q(status = status)
		familyservice_list = FamiliaServico.objects.filter(q)
		return render(request, 'familyservices.html', {'familyservice_list': familyservice_list})
@login_required(login_url='web:login')
def new_familyservice(request):
	if request.method == 'POST':
		form = FamilyServiceForm(request.POST)
		if form.is_valid():
			familyservice = FamiliaServico()
			familyservice.nome = request.POST['nome']
			familyservice.descricao = request.POST['descricao']
			familyservice.status = request.POST['status']
			if request.POST['org_id'] != '':
				familyservice.org_id = Organizacao.objects.get(pk=request.POST['org_id'])
			familyservice.save()
			return redirect('administrativo:familiaservico:detail_familyservice', pk=familyservice.pk)
	else :
		form = FamilyServiceForm()

	return render(request, 'new_familyservice.html', {'form': form})
@login_required(login_url='web:login')
def detail_familyservice(request, pk):
	familyservice = get_object_or_404(FamiliaServico, pk=pk)
	if familyservice is not None:
		return render(request, 'detail_familyservice.html', {'familyservice':familyservice})
	else :
		raise Http404("No familyservice found")
@login_required(login_url='web:login')
def edit_familyservice(request, pk):
	familyservice = get_object_or_404(FamiliaServico, pk=pk)
	if familyservice is not None:
		if request.method == 'POST':
			form = FamilyServiceForm(request.POST, instance=familyservice)
			if form.is_valid():
				familyservice.nome = request.POST['nome']
				familyservice.descricao = request.POST['descricao']
				familyservice.status = request.POST['status']
				if request.POST['org_id'] != '':
					familyservice.org_id = Organizacao.objects.get(pk=request.POST['org_id'])
				familyservice.save()
				return redirect('administrativo:familiaservico:detail_familyservice', pk=familyservice.pk)
		else :
			form = FamilyServiceForm(instance=familyservice)
			return render(request, 'edit_familyservice.html', {'form': form, 'pk': familyservice.pk})
	else :
		raise Http404("No familyservice found")
