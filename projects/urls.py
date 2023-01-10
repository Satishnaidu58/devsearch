
from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name="projects"),
    # pk = primark key, <> is used for dynamic content
    path('project/<str:pk>/', views.project, name="project"),
    
    path('create-project/', views.createProject, name="create-project"),
    
    path('update-project/<str:pk>', views.uopdateProject, name="update-project"),
    
    path('delete-project/<str:pk>', views.deleteProject, name="delete-project"),
]