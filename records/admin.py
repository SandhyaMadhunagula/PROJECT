from django.contrib import admin

# Register your models here.
from .models import Project, Part, Process, FailureRecord

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_id', 'project_name', 'created_at']
    search_fields = ['project_id', 'project_name', 'description']
    list_per_page = 20

@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ['part_number', 'make', 'grade', 'condition', 'created_at']
    list_filter = ['grade', 'condition']
    search_fields = ['part_number', 'make', 'description']
    list_per_page = 20

@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ['process_id', 'process_name', 'condition', 'created_at']
    search_fields = ['process_id', 'process_name', 'description']
    list_filter = ['condition']  # newly added 4/11/25 (mrng)
    list_per_page = 20

@admin.register(FailureRecord)
class FailureRecordAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'failure_type', 
        'get_part_or_process', 
        'project', 
        'failure_date', 
        'action_taken', 
        'created_by',
        'created_at'
    ]
    list_filter = ['failure_type', 'action_taken', 'failure_date', 'project']
    search_fields = [
        'failure_description', 
        'diagnosis', 
        'root_cause',
        'part__part_number',
        'process__process_id',
        'project__project_id'
    ]
    date_hierarchy = 'failure_date'
    list_per_page = 20
    
    fieldsets = (
        ('Failure Type', {
            'fields': ('failure_type', 'part', 'process', 'project')
        }),
        ('Failure Details', {
            'fields': ('failure_date', 'failure_description', 'diagnosis', 'root_cause', 'failure_confirmation')
        }),
        ('Action & Prevention', {
            'fields': ('action_taken', 'preventive_measures')
        }),
        ('Metadata', {
            'fields': ('created_by',),
            'classes': ('collapse',)
        }),
    )
    
    def get_part_or_process(self, obj):
        if obj.failure_type == 'PART' and obj.part:
            return obj.part.part_number
        elif obj.failure_type == 'PROCESS' and obj.process:
            return obj.process.process_id
        return '-'
    get_part_or_process.short_description = 'Part/Process'
    
    def save_model(self, request, obj, form, change):
        if not change:  # If creating new object
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


"""

from django.contrib import admin
from .models import Project, Part, Process, FailureRecord

# Customize Django Admin Titles
admin.site.site_header = "DLRL Failure Tracker"
admin.site.site_title = "DLRL Admin"
admin.site.index_title = "Welcome to DLRL Failure Tracker Administration"

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_id', 'project_name', 'created_at']
    search_fields = ['project_id', 'project_name', 'description']

@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ['part_number', 'make', 'grade', 'condition', 'created_at']
    list_filter = ['grade', 'condition']
    search_fields = ['part_number', 'make']

@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ['process_id', 'process_name', 'created_at']
    search_fields = ['process_id', 'process_name']

@admin.register(FailureRecord)
class FailureRecordAdmin(admin.ModelAdmin):
    list_display = ['failure_type', 'get_part_or_process', 'project', 'failure_date', 'action_taken']
    list_filter = ['failure_type', 'action_taken', 'failure_date']
    search_fields = ['failure_description', 'diagnosis', 'root_cause']
    
    def get_part_or_process(self, obj):
        if obj.failure_type == 'PART' and obj.part:
            return obj.part.part_number
        elif obj.failure_type == 'PROCESS' and obj.process:
            return obj.process.process_id
        return '-'
    get_part_or_process.short_description = 'Part/Process'
 
    """