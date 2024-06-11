from django.db import models

# Create your models here.

class Todo(models.Model):
    task_name = models.CharField(max_length=50)
    task_description = models.TextField()
    file = models.FileField(upload_to='file/')
    image = models.ImageField(upload_to='images/')
    start_date = models.DateField()
    end_date = models.DateField()
    status_of_task = models.CharField(max_length=50)