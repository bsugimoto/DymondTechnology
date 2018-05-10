from django.db import models
from django.utils import timezone

class Opportunity(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    due_date = models.DateTimeField(
            blank=True, null=True)

    class Meta:
        verbose_name = 'Opportunity'
        verbose_name_plural = 'Opportunites'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title