from django.shortcuts import render
from django.contrib import messages
from .forms import ThingForm

def home(request):
    if request.method == 'POST':
        form = ThingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thing added successfully!')
        else:
            messages.error(request, 'Error adding thing.')
    else:
        form = ThingForm()

    return render(request, 'home.html', {'form': form})
        
