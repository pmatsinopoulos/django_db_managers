import datetime
from django.db import models
from django.db import connection


class OpinionPollManager(models.Manager):
    def with_counts(self):
        with connection.cursor() as cursor:
            cursor.execute(
                """
                select p.id, p.question, p.poll_date, count(*)
                from polls_opinion_polls p 
                join polls_responses pr on pr.opinion_poll_id = p.id
                group by p.id, p.question, p.poll_date
                order by p.poll_date desc
                """
            )
            result_list = []
            for row in cursor.fetchall():
                p = self.model(id=row[0], question=row[1], poll_date=row[2])
                p.num_responses = row[3]
                result_list.append(p)
        return result_list


class OpinionPoll(models.Model):
    class Meta:
        db_table = 'polls_opinion_polls'

    question = models.CharField(default=None, max_length=255, unique=True)
    poll_date = models.DateField(auto_now_add=True)
    objects = OpinionPollManager()
