from django.db import models

# Create your models here.
class items(models.Model):
    objects = None
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='media')
    des=models.TextField()

    def __str__(self):
        return  self.name

class values(models.Model):
    objects = None
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='medias')
    des=models.TextField()

    def __str__(self):
        return self.name