from django.db import models

class Application(models.Model):
    appKey = models.CharField(max_length=60, unique=True, blank=False)
    name = models.CharField(max_length=255, blank=False)
    category = models.CharField(max_length=60, blank=False)
    downloads = models.IntegerField(max_length=10, blank=False)
    os = models.CharField(max_length=10, blank=True, null=True)
    source = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return self.name
