from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

def login_user(request):
	if request.user.is_authenticated:
		return redirect(reverse("example_list")) 
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('example_list')
		else:
			messages.success(request, ("Dados inválidos, tente novamente..."))	
			return redirect('login_user')	


	else:
		return render(request, 'authenticate/login.html', {})
	
@login_required()
def logout_user(request):
	logout(request)
	messages.success(request, ("Obrigado por usar o Datadomus!!"))
	return redirect('login_user')
