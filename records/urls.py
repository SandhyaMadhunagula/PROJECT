from .views import project_list
from django.urls import path
from .views import part_list
from .views import part_create
from .views import process_create, failure_create
from .views import failure_list
from .views import process_list
from .views import project_create
from .views import project_edit, project_delete

urlpatterns = [
    # ... (other url patterns if any)
    path("projects/", project_list, name="project-list"),
    path('parts/', part_list, name='part-list') ,
    path('parts/add/', part_create, name='part-add'),
    path('processes/add/', process_create, name='process-add'),
    path('failures/add/', failure_create, name='failure-add'),
    path('processes/', process_list, name='process-list'),
    path('failures/', failure_list, name='failure-list'),
     path('projects/add/', project_create, name='project-add'),
      path('projects/<int:pk>/edit/', project_edit, name='project-edit'),
    path('projects/<int:pk>/delete/', project_delete, name='project-delete'),

]

