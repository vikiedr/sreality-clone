from django.db import models

# Create your models here.
class Flat(models.Model):
    title = models.CharField(max_length=100)
    img_url = models.CharField(max_length=255)
    scrape_id = models.CharField(max_length=36)