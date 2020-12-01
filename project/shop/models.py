from django.db import models

# Create your models here.


class shop(models.Model):
    
    class Meta:
        verbose_name_plural = 'shops'

    name = models.CharField(max_length=200)
    address = models.TextField()
    rating = models.PositiveIntegerField(default = 2)