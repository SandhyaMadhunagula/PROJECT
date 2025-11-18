from django.db import models

# Create your models here.from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    """Store project information"""
    project_id = models.CharField(max_length=50, unique=True, verbose_name="Project ID")
    project_name = models.CharField(max_length=200, verbose_name="Project Name")
    description = models.TextField(blank=True, verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.project_id} - {self.project_name}"
    
    class Meta:
        ordering = ['project_id']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class Part(models.Model):
    """Store part information"""
    GRADE_CHOICES = [
        ('COMMERCIAL', 'Commercial'),
        ('INDUSTRIAL', 'Industrial'),
        ('MILITARY', 'Military'),
        ('SPACE', 'Space'),
    ]
    
    CONDITION_CHOICES = [
        ('NEW', 'New'),
        ('OLD', 'Old'),
    ]
    
    part_number = models.CharField(max_length=100, unique=True, verbose_name="Part Number")
    make = models.CharField(max_length=100, verbose_name="Make/Manufacturer")
    grade = models.CharField(max_length=20, choices=GRADE_CHOICES, verbose_name="Grade")
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES, verbose_name="Condition")
    description = models.TextField(blank=True, verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.part_number} - {self.make}"
    
    class Meta:
        ordering = ['part_number']
        verbose_name = 'Part'
        verbose_name_plural = 'Parts'


class Process(models.Model):
    CONDITION_CHOICES = [
        ('NEW', 'New'),
        ('OLD', 'Old'),
    ]
    """Store process information"""
    process_id = models.CharField(max_length=50, unique=True, verbose_name="Process ID")
    process_name = models.CharField(max_length=200, verbose_name="Process Name")
    description = models.TextField(blank=True, verbose_name="Description")
    #condition = models.CharField(max_length=10, choices=CONDITION_CHOICES, verbose_name="Condition")
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.process_id} - {self.process_name}"
    
    class Meta:
        ordering = ['process_id']
        verbose_name = 'Process'
        verbose_name_plural = 'Processes'


class FailureRecord(models.Model):
    """Main failure tracking record"""
    ACTION_CHOICES = [
        ('REPAIR', 'Repair'),
        ('REWORK', 'Rework'),
    ]
    
    FAILURE_TYPE_CHOICES = [
        ('PART', 'Part'),
        ('PROCESS', 'Process'),
    ]
    
    # Type of failure
    failure_type = models.CharField(max_length=10, choices=FAILURE_TYPE_CHOICES,verbose_name="Failure Type")
    
    # Related Part or Process (one will be selected based on failure_type)
    part = models.ForeignKey(
        Part, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='failures',
        verbose_name="Part"
    )
    process = models.ForeignKey(
        Process, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='failures',
        verbose_name="Process"
    )
    
    # Related Project
    project = models.ForeignKey(
        Project, 
        on_delete=models.CASCADE, 
        related_name='failures',
        verbose_name="Project"
    )
    
    # Failure details
    failure_date = models.DateTimeField(verbose_name="Failure Date & Time")
    failure_description = models.TextField(verbose_name="Failure Description")
    diagnosis = models.TextField(verbose_name="Diagnosis")
    root_cause = models.TextField(verbose_name="Root Cause")
    failure_confirmation = models.TextField(verbose_name="Failure Confirmation")
    
    # Action taken
    action_taken = models.CharField(max_length=10,choices=ACTION_CHOICES,verbose_name="Action Taken")
    preventive_measures = models.TextField(verbose_name="Preventive Measures")
    
    # Metadata
    created_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        verbose_name="Created By"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    
    class Meta:
        ordering = ['failure_date']  #'-failure_date'
        verbose_name = 'Failure Record'
        verbose_name_plural = 'Failure Records'
    
    def __str__(self):
        if self.failure_type == 'PART' and self.part:
            return f"Failure: {self.part.part_number} - {self.failure_date.strftime('%Y-%m-%d')}"
        elif self.failure_type == 'PROCESS' and self.process:
            return f"Failure: {self.process.process_id} - {self.failure_date.strftime('%Y-%m-%d')}"
        else:
            return f"Failure Record - {self.failure_date.strftime('%Y-%m-%d')}"
