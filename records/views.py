from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .models import Part 
from .forms import PartForm  # add at the top
from .forms import ProcessForm, FailureRecordForm  # Add at the top
from .models import FailureRecord
from .models import Process
from .forms import ProjectForm
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q

# Create your views here.
def apppr(request):
    return HttpResponse("Hi!! Hello Welcome")


def project_list(request):
    query = request.GET.get('q')
    projects = Project.objects.all()
    if query:
        projects = projects.filter(
            Q(project_name__icontains=query) | Q(description__icontains=query)
        )
    return render(request, 'records/project_list.html', {'projects': projects})


def part_list(request):
    # Fetch all rows in the Part table from the database, sorted by part_id
    parts = Part.objects.all().order_by('part_number')
    # Render the web page 'part_list.html', passing the "parts" data
    return render(request, 'records/part_list.html', {'parts': parts})


def process_list(request):
    processes = Process.objects.all().order_by('id')  # Or any field you want
    return render(request, 'records/process_list.html', {'processes': processes})

def failure_list(request):
    failures = FailureRecord.objects.all().order_by('id')  # Adjust ordering as you want
    return render(request, 'records/failure_list.html', {'failures': failures})


def part_create(request):
    if request.method == "POST":
        form = PartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('part-list')  # after saving, go back to the list
    else:
        form = PartForm()
    return render(request, 'records/part_form.html', {'form': form})

def process_create(request):
    if request.method == "POST":
        form = ProcessForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('process-list')
    else:
        form = ProcessForm()
    return render(request, 'records/process_form.html', {'form': form})

def failure_create(request):
    if request.method == "POST":
        form = FailureRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('failure-list')
    else:
        form = FailureRecordForm()
    return render(request, 'records/failure_form.html', {'form': form})


def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project-list')
    else:
        form = ProjectForm()
    return render(request, 'records/project_form.html', {'form': form})

#Edit view
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project-list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'records/project_form.html', {'form': form, 'project': project})

#Delete View
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project-list')
    return render(request, 'records/project_confirm_delete.html', {'project': project})
