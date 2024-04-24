from django.contrib.auth.models import User
from django.db import models
from med_farm.models import Organisation


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    organisation = models.ForeignKey(Organisation, related_name='user_profiles', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.user.username} - {self.organisation.name if self.organisation else 'None'}"