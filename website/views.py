from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from codes.forms import CodeForm
from accounts.models import CustomUser

# Create your views here.

@login_required
def home(request):
	return render(request, 'website/home.html', {})

def auth_view(request):
	form = AuthenticationForm()
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		authenticate(request, username=username, password=password)
		if user is not None:
			request.session['pk'] = user.pk
			return redirect('verify') 
	return render(request, 'website/auth.html', {'form': form})	
	
def verify_view():
	form = CodeForm(request.POST or None)
	pk = request.session.get('pk')
	if pk:
		user = CustomUser.objects.get(pk=pk)
		code = user.code
		code_user = f"{user.username}: {user.code}"
		if not request.POST:
			# Send SMS.
			pass
		if form.is_valid():
			num = form.clean_data.get('number')	

			if str(code) == num:
				code.save() 
				login(request, user)
				return redirect('home')
			else:
				return redirect('login')
	return render(request, 'website/verify.html', {'form': form})				