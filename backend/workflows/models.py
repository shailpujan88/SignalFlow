from django.db import models
from django.contrib.auth.models import User

class Workflow(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    definition = models.JSONField()  # rules + steps
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
