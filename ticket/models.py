from django.db import models

# from UploadMedia.models import UploadMedia
from category.models import Category
from ticket.utils import unique_slugify
from upload_media.models import UploadMedia


class Ticket(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
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
    image = models.ManyToManyField(UploadMedia, null=True, blank=False, related_name='ticket_images')
    email = models.EmailField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', null=True, blank=False)
    phone_number = models.CharField(max_length=20,default=0)

    def __str__(self):
        return format(self.name)


    def save(self, **kwargs):
        slug_str = "%s" % (self.name)
        unique_slugify(self, slug_str)
        super(Ticket, self).save()