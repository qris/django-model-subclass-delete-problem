from django.contrib.sessions.models import Session
from django.db import models

class SessionWithExtraField(Session):
    extra_field = models.CharField(max_length=10)
