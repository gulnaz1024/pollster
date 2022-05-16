from django.shortcuts import render
from django.shortcuts import render
from .forms import PollsterForm
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'pages/index.html')

def user_register(request):
    form=UserCreationForm()
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

        else:
            form = UserCreationForm()

    context={
        'form': form,
        'title':'Register',
        }

    return render(request,'pages/register.html',context)