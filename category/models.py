from django.db import models

from ticket.utils import unique_slugify


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100,)
    slug = models.SlugField(max_length=50, unique=True, )
    description = models.TextField()
    public = models.BooleanField(default=True,)

    def save(self, **kwargs):
        slug_str = "%s" % (self.title,)
        unique_slugify(self, slug_str)
        super(Category, self).save(**kwargs)