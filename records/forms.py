from django import forms
from .models import Part
from .models import Process, FailureRecord
from .models import Project



#for parts 
class PartForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ['part_number', 'make', 'grade', 'condition', 'description']



class ProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = ['process_name', 'condition', 'description']

class FailureRecordForm(forms.ModelForm):
    class Meta:
        model = FailureRecord
        fields = [
            'failure_type', 'part', 'process', 'project',
            'failure_date', 'failure_description',
            'diagnosis', 'root_cause', 'failure_confirmation',
            'action_taken', 'preventive_measures', 'created_by'
        ]

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'description']  # Adjust for your real fields!