from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import AuthenticationForm
from sys import path_importer_cache
from PIL import Image,ImageDraw, ImageFont
import os
from fileinput import filename

def index(request):
    return render(request, 'pages/index.html')

def user_register(request):
    form=UserCreationForm()
    context= {
        'form':form,
        'title':'Register',
            }
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            for filename in os.listdir('./media'):
                path_to_img = './media/' + str(filename)
                img = Image.open(path_to_img)
                img = img.crop((0, 0, 1080, 1080))
                
                grayscale = img.convert('L')
                # grayscale.show()
                filename = filename.split('.')
                path_to_edited_img = './media/' + filename[0] + '.png'
                grayscale.save(path_to_edited_img)
                os.remove(path_to_img)
            return render(request, 'pages/register_done.html',context)
            
    return render(request, 'pages/register.html',context)
    
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
