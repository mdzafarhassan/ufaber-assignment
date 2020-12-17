from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name="index"),
    path('project/create-new/', views.project_create, name="project_view"),
    path('project/<int:project_id>/delete/',
         views.project_delete, name="project_delete"),
    path('project/<int:project_id>/update',
         views.project_update, name="project_update"),
]
