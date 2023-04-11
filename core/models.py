from django.db import models

# Create your models here.

class Assets(models.Model):
    asset_name = models.CharField(max_length=59)
    asset_type = models.CharField(max_length=50)
    asset_quantity = models.IntegerField()

    def __str__(self):
        return self.asset_name