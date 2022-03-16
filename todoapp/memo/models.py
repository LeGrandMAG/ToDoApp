from django.db import models

# Create your models here.
class Memo(models.Model):
    title = models.CharField(max_length=100, null=True, blank=False)
    description = models.TextField(max_length=145, blank=True)
    created = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

