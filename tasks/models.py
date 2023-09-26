from django.db import models
from django.contrib.auth import get_user_model


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
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
