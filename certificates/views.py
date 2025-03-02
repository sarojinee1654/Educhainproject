from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Certificate
from .forms import CertificateForm
from django.contrib import messages



@login_required
def issue_certificate(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            certificate = form.save(commit=False)
            certificate.issuer = request.user
            certificate.save()
            messages.success(request, 'Certificate issued successfully!')
            return redirect('verify_certificate')
    else:
        form = CertificateForm()
    return render(request, 'issue_certificate.html', {'form': form})

def verify_certificate(request):
    if request.method == 'POST':
        certificate_id = request.POST.get('certificate_id')
        try:
            certificate = Certificate.objects.get(certificate_id=certificate_id)
            certificate.verified = True
            certificate.save()
            messages.success(request, 'Certificate verified successfully!')
        except Certificate.DoesNotExist:
            messages.error(request, 'Certificate not found!')
    return render(request, 'verify_certificate.html')