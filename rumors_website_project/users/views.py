from django.shortcuts import render, redirect
from django.contrib import messages 
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can now login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

