from django.db import models

# Create your models here.
class Todoitem(models.Model):
    todo_text=models.CharField(max_length=100,null=False)
    todo_status=models.CharField(max_length=8,default="NOT DONE")

    def __str__(self) -> str:
        return self.todo_text
