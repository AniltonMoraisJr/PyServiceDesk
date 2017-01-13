from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404, JsonResponse
from django.core import serializers
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def login(request):
	if request.method == 'POST':
		username = request.POST['user']
		password = request.POST['pass']
		user = authenticate(username = username, password = password)
		if user is not None:
			auth_login(request,user)
			return redirect('administrativo:manager')
		else:
			return render(request, 'login.html', {'error': 'Usuario e/ou Senha errados !'})
	else:
		return render(request, 'login.html')
def logout(request):
	if request.user.is_authenticated:
		auth_logout(request)
		return redirect('web:login')
