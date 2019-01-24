from django.db import models
from django.utils import timezone

class Ticket(models.Model):

    FEATURE = 'F'
    BUG = 'B' 
    TICKET_TYPE_CHOICES = (
        (FEATURE, 'Feature'),
        (BUG, 'Bug')
    )
    TO_DO = 'to_do'
    DOING = 'doing'
    DONE = 'done'
    STATUS_CHOICES = (
        (TO_DO,'to_do'),
        (DOING,'doing'),
        (DONE,'done')
    )

    title = models.CharField(max_length=254, default='')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    votes = models.IntegerField(default=0)
    ticket_type = models.CharField(max_length=10, choices=TICKET_TYPE_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created_by = models.CharField(max_length=254, default='')

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=254, default='')
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

