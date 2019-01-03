from django.db import models


class Workspace(models.Model):
    deal_type = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    price = models.IntegerField()
    area = models.IntegerField()
    photos = models.FileField()
