from django.core.management.base import BaseCommand
from faker import Faker
from hangarin.models import Task, SubTask, Note, Priority, Category
from django.utils import timezone

class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self, *args, **kwargs):
        self.create_task(10)
        self.create_subtask(10)
        self.create_note(10)

    def create_task(self, count):
        fake = Faker()

        for _ in range(count):
            Task.objects.create(
                task_name = fake.sentence(nb_words=5),
                task_description = fake.paragraph(nb_sentences=3),
                task_deadline = timezone.make_aware(fake.date_time_this_month()),
                task_status = fake.random_element(elements=["Pending", "In Progress", "Completed"]),
                task_priority = Priority.objects.order_by('?').first(),
                task_category = Category.objects.order_by('?').first(),
            )

    def create_subtask(self, count):
        fake = Faker()

        for _ in range(count):
            SubTask.objects.create(
                parent_task = Task.objects.order_by('?').first(),
                subtask_title = fake.sentence(nb_words=5),
                subtask_status = fake.random_element(elements=["Pending", "In Progress", "Completed"]),
            )

    def create_note(self, count):
            fake = Faker()
    
            for _ in range(count):
                Note.objects.create(
                    task_note = Task.objects.order_by('?').first(),
                    note_content = fake.paragraph(nb_sentences=3),
                )


