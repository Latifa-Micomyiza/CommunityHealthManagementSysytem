# health/views.py

from django.shortcuts import render, redirect
from .models import Patient, Appointment, MedicalRecord
from .forms import PatientForm

def home(request):
    patients = Patient.objects.all()
    return render(request, 'health/home.html', {'patients': patients})

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PatientForm()
    return render(request, 'health/add_patient.html', {'form': form})
