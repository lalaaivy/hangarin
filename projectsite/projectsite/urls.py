from django.contrib import admin
from django.urls import path
from hangarin.views import HomePageView, TaskListView, TaskCreateView
from hangarin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('task_list', TaskListView.as_view(), name='task-list'),
    path('task_list/add', TaskCreateView.as_view(), name='task-add'),
]
