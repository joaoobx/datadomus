from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_user(request):
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
	
def logout_user(request):
	logout(request)
	messages.success(request, ("Obrigado por usar o Datadomus!!"))
	return redirect('login_user')
