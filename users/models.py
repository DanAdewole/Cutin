from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
	username = None
	email = models.EmailField(_('email address'), unique=True)

	USERNAME_FIELD: str = 'email'
	REQUIRED_FIELDS = []

	objects = CustomUserManager()

	name = models.CharField(blank=True, max_length=100)
	
	def __str__(self):
		return self.email
