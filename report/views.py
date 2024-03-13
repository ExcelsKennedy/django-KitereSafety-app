from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PhotoReportForm
from django.contrib.auth.decorators import login_required 

def report(request):
    return render(request, 'report/home.html')

@login_required
def audio(request):
    return render(request, 'report/audio-report.html')

@login_required
def photo_success(request): 
    return render(request, 'report/photo-success.html')

@login_required
def photo_report_view(request):
    if request.method == 'POST':
        form = PhotoReportForm(request.POST, request.FILES)
        if form.is_valid():
            photo_report = form.save(commit=False)
            photo_report.user = request.user
            photo_report.save()
            messages.success(request, f'Photo report submitted successfully!')
            return redirect('photo-success')  # Redirect to a success URL
    else:
        form = PhotoReportForm()
    return render(request, 'report/photo_report_form.html', {'form': form}) 