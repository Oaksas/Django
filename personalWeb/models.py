from django.db import models

class gallerySource(models.Model):
 img=models.ImageField(upload_to='pics')
 desc=models.CharField(max_length=100)
