from django.shortcuts import render, redirect 
from .forms import SignupForm

# Create your views here.

def index(request):
    return render(request, 'core/index.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form 
    })


def about(request):
    return render(request, 'core/about.html')  


def careers(request):
    return render(request, 'core/careers.html') 


def privacy(request):
    return render(request, 'core/privacy.html') 


def terms(request):
    return render(request, 'core/terms.html') 