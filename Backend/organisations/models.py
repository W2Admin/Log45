import uuid
from django.db import models

class Industry(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Organisation(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    address = models.TextField(default='1')
    industry = models.ForeignKey(Industry, related_name='organisation_industry', on_delete=models.CASCADE, default=None)
    org_uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f"{self.name} - \"{self.description}\" (UID: {self.org_uid})"
