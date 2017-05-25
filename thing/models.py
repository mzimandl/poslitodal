from django.db import models
from django.utils import timezone

class Thing(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100)
    text = models.TextField()
    add_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey('category.Category')

    def __str__(self):
        return self.title