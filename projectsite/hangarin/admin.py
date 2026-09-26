from django.contrib import admin

from .models import Priority, Category, Task, SubTask, Note

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('priority_name',)
    search_fields = ('priority_name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    search_fields = ('category_name',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'task_status', 'task_deadline', 'task_priority', 'task_category',)
    search_fields = ('task_name', 'task_description',)
    list_filter = ('task_status','task_priority', 'task_category',)

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('subtask_title', 'subtask_status', 'parent_task',)
    search_fields = ('subtask_title',)
    list_filter = ('subtask_status',)

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('task_note', 'note_content', 'created_at',)
    search_fields = ('note_content',)
    list_filter = ('created_at',)


    