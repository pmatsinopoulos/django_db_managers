from __future__ import unicode_literals

from django.db import models
from managers import AuthorsManager
from managers import EditorsManager


class Person(models.Model):
    class Meta:
        db_table = 'people_people'

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    first_name = models.CharField(max_length=255, default=None)
    last_name = models.CharField(max_length=255, default=None)
    role = models.CharField(max_length=1, choices=(('A', 'Author'), ('E', 'Editor')))

    people = models.Manager()
    authors = AuthorsManager()
    editors = EditorsManager()

