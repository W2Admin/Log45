from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionMixin, BaseUserManager

class UserAccountManager(BaseUserManager):
    # def create_user()
        

class UserAccount(AbstractBaseUser, PermissionMixin):
    email = models.EmailField(max_length=255, unique=True)