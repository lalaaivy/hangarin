from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from hangarin.models import Task, SubTask, Note, Category, Priority
from hangarin.forms import TaskForm, SubTaskForm, NoteForm, CategoryForm, PriorityForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils import timezone

class HomePageView(ListView):   
    model = Task
    context_object_name = 'home'
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["total_task"] = Task.objects.count()

        context["total_subtask"] = SubTask.objects.count()

        context["total_note"] = Note.objects.count()


        today = timezone.now().date()
        count = (
            Task.objects.filter(
                created_at__year=today.year
            )
            .values("task_name")
            .distinct()
            .count()
        )

        context["tasks_added_this_year"] = count
        return context

# TASK

class TaskListView(ListView):
    model = Task
    context_object_name = 'task'
    template_name = "task_list.html"
    paginate_by = 5
    ordering = ["task_name"]

    def get_queryset(self):
        qs = super().get_queryset() 
        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(
                Q(task_name__icontains=query) |
                Q(task_status__icontains=query) |
                Q(task_deadline__icontains=query) |
                Q(task_priority__priority_name__icontains=query) |
                Q(task_category__category_name__icontains=query)
            )

        return qs

    def get_ordering(self):
            allowed = ["task_name", "task_priority__priority_name", "task_category__category_name"]
            sort_by = self.request.GET.get("sort_by")
    
            if sort_by in allowed:
                return sort_by
    
            return "task_name"

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_del.html'
    success_url = reverse_lazy('task-list')

# SUBTASK

class SubTaskListView(ListView):
    model = SubTask
    context_object_name = 'sub-task'
    template_name = "subtask_list.html"
    paginate_by = 5
    ordering = ["subtask_title"]

    def get_queryset(self):
        qs = super().get_queryset() 
        query = self.request.GET.get('q')
    
        if query:
            qs = qs.filter(
                Q(parent_task__task_name__icontains=query) |
                Q(subtask_title__icontains=query) |
                Q(subtask_status__icontains=query)
            )
    
        return qs

    def get_ordering(self):
        allowed = ["subtask_title", "parent_task__task_name"]
        sort_by = self.request.GET.get("sort_by")

        if sort_by in allowed:
            return sort_by

        return "subtask_title"

class SubTaskCreateView(CreateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')

class SubTaskUpdateView(UpdateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')

class SubTaskDeleteView(DeleteView):
    model = SubTask
    template_name = 'subtask_del.html'
    success_url = reverse_lazy('subtask-list')

# NOTES

class NoteListView(ListView):
    model = Note
    context_object_name = 'note'
    template_name = "note_list.html"
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset() 
        query = self.request.GET.get('q')
        
        if query:
            qs = qs.filter(
                Q(task_note__task_name__icontains=query) |
                Q(note_content__icontains=query) 
            )
        
        return qs

    def get_ordering(self):
                allowed = ["task_note__task_name", "note_content"]
                sort_by = self.request.GET.get("sort_by")
        
                if sort_by in allowed:
                    return sort_by
        
                return "note_content"

class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note_del.html'
    success_url = reverse_lazy('note-list')

# CATEGORY

class CategoryListView(ListView):
    model = Category
    context_object_name = 'category'
    template_name = "category_list.html"
    paginate_by = 5

    def get_queryset(self):
            qs = super().get_queryset() 
            query = self.request.GET.get('q')
            
            if query:
                qs = qs.filter(
                    Q(category_name__icontains=query) 
                )
            
            return qs

    def get_ordering(self):
                    allowed = ["category_name"]
                    sort_by = self.request.GET.get("sort_by")
            
                    if sort_by in allowed:
                        return sort_by
            
                    return "category_name"

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_del.html'
    success_url = reverse_lazy('category-list')

# PRIORITY

class PriorityListView(ListView):
    model =  Priority
    context_object_name = 'priority'
    template_name = "priority_list.html"
    paginate_by = 5

    def get_queryset(self):
                qs = super().get_queryset() 
                query = self.request.GET.get('q')
                
                if query:
                    qs = qs.filter(
                        Q(priority_name__icontains=query) 
                    )
                
                return qs

    def get_ordering(self):
                        allowed = ["priority_name"]
                        sort_by = self.request.GET.get("sort_by")
                
                        if sort_by in allowed:
                            return sort_by
                
                        return "priority_name"

 

class PriorityCreateView(CreateView):
    model =  Priority
    form_class = PriorityForm
    template_name = 'priority_form.html'
    success_url = reverse_lazy('priority-list')

class PriorityUpdateView(UpdateView):
    model =  Priority
    form_class = PriorityForm
    template_name = 'priority_form.html'
    success_url = reverse_lazy('priority-list')

class PriorityDeleteView(DeleteView):
    model =  Priority
    template_name = 'priority_del.html'
    success_url = reverse_lazy('priority-list')
