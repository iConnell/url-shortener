from django.db import models

# Create your models here.

class Link(models.Model):
    #longUrl = models.CharField(max_length=500)
    longUrl = models.URLField(null=True, blank=True)
    shortUrl = models.CharField(max_length=15)

    def __str__(self):
        return self.shortUrl