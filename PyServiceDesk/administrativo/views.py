from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
# Create your views here.
@login_required(login_url='web:login')
def manager(request):
	return render(request, 'administrativo.html')
