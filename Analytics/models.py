from django.db import models

class Application(models.Model):
    appKey = models.CharField(max_length=60, unique=True, blank=False)
    name = models.CharField(max_length=255, blank=False)
    category = models.CharField(max_length=60, blank=False)
    downloadsA = models.IntegerField(max_length=10, blank=False)
    downloadsM = models.IntegerField(max_length=10, blank=False)
    downloadsW = models.IntegerField(max_length=10, blank=False)
    downloadsT = models.IntegerField(max_length=10, blank=False)
    os = models.CharField(max_length=13, blank=True, null=True)
    account = models.CharField(max_length=10, blank=False)
    revenueA = models.CharField(max_length=8, blank=False)
    revenueM = models.CharField(max_length=8, blank=False)
    revenueW = models.CharField(max_length=8, blank=False)
    revenueT = models.CharField(max_length=8, blank=False)

    def __str__(self):
        return self.name


class Date(models.Model):
    dateAppannie = models.CharField(max_length=20, blank=False)
    dateExcel = models.CharField(max_length=20, blank=False)