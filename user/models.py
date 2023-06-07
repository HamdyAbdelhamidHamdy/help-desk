from django.db import models

# Create your models here.


class UserMail(models.Model):
    mail = models.EmailField()

    def __str__(self):
        return self.mail
