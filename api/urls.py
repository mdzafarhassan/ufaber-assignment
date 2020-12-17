from django.urls import path
from . import views

urlpatterns = [
    # PROJECTS API URLS
    path('', views.project_all, name="all_projects", ),
    path('<int:project_id>/', views.project_detail, name="detail"),
    path('create_project/', views.project_create, name="create"),
    path('<int:project_id>/update', views.project_update, name="update"),
    path('<int:project_id>/delete/', views.project_delete, name="delete"),

    # TASKS API URLS
    path('task/', views.task_all, name="all_task"),
    path('<int:project_id>/task/', views.task_all, name="project_all_task"),
    path('<int:project_id>/<int:task_id>/',
         views.task_detail, name="task_view"),
    path('<int:project_id>/create_task/',
         views.task_create, name="task_create"),
    path('<int:project_id>/<int:task_id>/update',
         views.task_update, name="task_update"),
    path('<int:project_id>/<int:task_id>/delete/',
         views.task_delete, name="task_delete"),


]
