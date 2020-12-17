from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name="index"),
    path('project/create-new/', views.project_create, name="project_view"),
    # path('project/<int:project_id>', views.project_details, name="project_view"),
]
