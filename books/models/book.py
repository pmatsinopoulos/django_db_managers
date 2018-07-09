from django.db import models


class DahlManager(models.Manager):
    def get_queryset(self):
        return super(DahlManager, self).get_queryset().filter(author='Roald Dahl')


class Book(models.Model):
    class Meta:
        db_table = 'books_books'

    title = models.CharField(max_length=255, default=None, unique=True)
    author = models.CharField(max_length=255, default=None)

    objects = models.Manager()
    dahl_objects = DahlManager()

    @classmethod
    def count(cls):
        return cls.objects.count()
