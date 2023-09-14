from django.db import models

class Task(models.Model):
    STATUS = (
        (True, 'Done'),
        (False, 'Doing')
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.BooleanField(
        choices=STATUS,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
