import uuid
from django.db import models

class Organisation(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    org_uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f"{self.name} - \"{self.description}\" (UID: {self.org_uid})"
