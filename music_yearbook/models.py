from django.db import models
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# Author is our custom user model
class Author(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bio = models.TextField(blank=True)

