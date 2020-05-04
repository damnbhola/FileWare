from django.db import models
import random
import string


def at():
    return ''.join(random.sample(string.ascii_letters, 8))


class File(models.Model):
    file = models.FileField(upload_to='file')
    file_name = models.CharField(max_length=50)
    up_date = models.DateTimeField()
    location = models.CharField(max_length=8, default=at, blank=True)

    def __str__(self):
        return self.file_name
