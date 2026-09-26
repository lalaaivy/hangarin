from django.contrib import admin
from django.urls import path
from hangarin.views import HomePageView, TaskList
from hangarin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('task_list', TaskList.as_view(), name='task-list'),
]
