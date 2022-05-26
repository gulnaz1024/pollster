from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    return render(request, 'pages/index.html')

def user_register(request):
    form=UserCreationForm()
    context={
        'form': form,
        'title':'Register',
        }
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print('Form is passed')
            return render(request,'pages/index.html',context)

        else:
            form = UserCreationForm()
            print('Else block')
            return render(request,'pages/register.html',context)
    
    return render(request,'pages/register.html',context) 
    
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return render(request, 'pages/index.html')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="pages/login.html", context={"login_form":form})

    