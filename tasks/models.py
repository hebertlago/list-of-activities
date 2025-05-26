from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('A', 'In Progress'),
        ('C', 'Completed'),
    ]    
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    
    def __str__(self) -> str:
        return self.title
