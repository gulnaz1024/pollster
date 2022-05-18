from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

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
    

    