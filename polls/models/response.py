from django.db import models
from opinion_poll import OpinionPoll


class Response(models.Model):
    class Meta:
        db_table = 'polls_responses'

    opinion_poll = models.ForeignKey(OpinionPoll, on_delete=models.CASCADE)
    person_name = models.CharField(max_length=255, default=None)
    response = models.TextField()

