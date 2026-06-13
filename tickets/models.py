from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings


class Ticket(models.Model):

    STATUS_CHOICES = [
        ("open", "Open"),
        ("in_progress", "In Progress"),
        ("resolved", "Resolved"),
    ]

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tickets"
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    category = models.CharField(
        max_length=50
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="open"
    )

    ai_suggestion = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title