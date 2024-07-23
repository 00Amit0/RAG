from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.image.name
