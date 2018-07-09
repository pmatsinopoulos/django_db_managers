from django.db import models


class AuthorsManager(models.Manager):
    def get_queryset(self):
        return super(AuthorsManager, self).get_queryset().filter(role='A')