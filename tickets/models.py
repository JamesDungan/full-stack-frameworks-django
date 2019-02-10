from django.db import models
from django.utils import timezone

class Ticket(models.Model):

    FEATURE = 'Feature'
    BUG = 'Bug' 
    TICKET_TYPE_CHOICES = (
        (FEATURE, 'Feature'),
        (BUG, 'Bug')
    )
    TO_DO = 'To Do'
    DOING = 'Doing'
    DONE = 'Done'
    STATUS_CHOICES = (
        (TO_DO,'To Do'),
        (DOING,'Doing'),
        (DONE,'Done')
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

class Vote(models.Model):
    username = models.CharField(max_length=150)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("username", "ticket"),)





