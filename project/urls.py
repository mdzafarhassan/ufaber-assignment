from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.project_list, name="project_list"),
    path('project/<int:project_id>/', views.project_view, name="project_view"),
    path('project/create-new/', views.project_create, name="project_view"),
    path('project/<int:project_id>/delete/',
         views.project_delete, name="project_delete"),
    path('project/<int:project_id>/update',
         views.project_update, name="project_update"),

    path('project/<int:project_id>/task-new/',
         views.task_create, name="task_create"),

    path('project/<int:project_id>/<int:task_id>/delete/',
         views.task_delete, name="task_delete"),

    path('project/<int:project_id>/<int:task_id>/update',
         views.task_update, name="task_update")
]
urlpatterns += staticfiles_urlpatterns()
