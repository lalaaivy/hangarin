from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Priority(BaseModel):
    priority_name = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Priority"
        verbose_name_plural = "Priorities" 

    def __str__(self):
        return self.priority_name

class Category(BaseModel):
    category_name = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories" 

    def __str__(self):
            return self.category_name

class Task(BaseModel):
    task_name = models.CharField(max_length=150)
    task_description = models.TextField(max_length=200)
    task_deadline = models.DateField()
    task_status = models.CharField(max_length=50,choices=[("Pending", "Pending"),("In Progress ", "In Progress"),("Completed", "Completed"), ],default="pending")
    task_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    task_priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.task_name

class Note(BaseModel):
    task_note = models.ForeignKey(Task, on_delete=models.CASCADE)
    note_content = models.TextField(max_length=200)

    def __str__(self):
            return self.task_note.task_name

class SubTask(BaseModel):
    parent_task = models.ForeignKey(Task, on_delete=models.CASCADE)
    subtask_title = models.CharField(max_length=150)
    subtask_status = models.CharField(max_length=50,choices=[("Pending", "Pending"),("In Progress ", "In Progress"),("Completed", "Completed"), ],default="pending")

    def __str__(self):
            return self.subtask_title




