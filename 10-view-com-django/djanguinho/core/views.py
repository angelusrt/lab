from django.shortcuts import render, get_object_or_404
from .models import Note

def home(request):
    context = {'name': 'Angelus', 'items': ['dbt', 'Airflow', 'BigQuery']}
    return render(request, 'core/home.html', context)

def note_list(request):
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'core/note_list.html', {'notes': notes})

def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'core/note_detail.html', {'note': note})
