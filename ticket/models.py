from django.db import models


class Ticket(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=(
        ('1', 'Open'),
        ('2', 'Reopened'),
        ('3', 'Resolved'),
        ('4', 'Closed'),
        ('5', 'Duplicate'),
    ), max_length=1,default='1')
    priority = models.CharField(choices=(
        ('critical', 'Critical'),
        ('high', 'High'),
        ('normal', 'Normal'),
        ('low', 'Low'),
        ('verylow', 'Very Low'),
    ), max_length=20,default='low')
    image = models.ImageField(upload_to='tickets', null=True, blank=False)

    def __str__(self):
        return format(self.name)


class Media(models.Model):
    file = models.FileField(upload_to='media/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
