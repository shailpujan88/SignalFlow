from django.db import models
from workflows.models import Workflow

class Execution(models.Model):
    STATUS_CHOICES = (
        ("PENDING", "Pending"),
        ("RUNNING", "Running"),
        ("WAITING", "Waiting for Approval"),
        ("SUCCESS", "Success"),
        ("FAILED", "Failed"),
    )

    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    input_data = models.JSONField()
    output_data = models.JSONField(null=True, blank=True)
    error = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
