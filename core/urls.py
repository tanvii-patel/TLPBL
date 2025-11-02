from django.urls import path
from . import views
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),

    path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
path('dashboard/', views.dashboard, name='dashboard'),
    path('timetable/', views.timetable, name='timetable'),
    path('timetable/edit/<int:pk>/', views.timetable_edit, name='timetable_edit'),
   path('timetable/delete/<int:pk>/', views.delete_timetable, name='timetable_delete'),
path('logout/', views.logout_view, name='logout'),


    path('tasks/', views.tasks, name='tasks'),
    path('tasks/edit/<int:id>/', views.task_edit, name='task_edit'),
    path('tasks/toggle/<int:id>/', views.task_toggle, name='task_toggle'),
    path('tasks/delete/<int:id>/', views.task_delete, name='delete_task'),


    path('resources/', views.resources, name='resources'),
   path('resources/delete/<int:id>/', views.resource_delete, name='delete_resource'),

]
