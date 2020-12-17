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
]
urlpatterns += staticfiles_urlpatterns()
