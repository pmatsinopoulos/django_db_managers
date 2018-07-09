from django.db import models


class EditorsManager(models.Manager):
    def get_queryset(self):
        return super(EditorsManager, self).get_queryset().filter(role='E')
