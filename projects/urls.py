from django.urls import path
from devsearch.settings import MEDIA_ROOT
from . import views
from django.contrib import admin

urlpatterns = [
    path('',views.projects , name = 'projects'),
    path('project/<str:pk>/', views.project,name = 'project'),
    
    path('create-project/',views.CreateProject,name = 'create-project'),
    path('Update-project/<str:pk>/',views.UpdateProject,name= 'update-project'),
    path('Delete-project/<str:pk>/',views.DeleteProject,name= 'delete-project'),
]

