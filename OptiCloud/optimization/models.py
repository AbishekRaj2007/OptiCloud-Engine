from django.db import models

# Create your models here.


class ResourceUsage(models.Model):
    resource_id = models.CharField(max_length=100)
    cpu_usage = models.FloatField()
    memory_usage = models.FloatField()
    cost = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.resource_id
