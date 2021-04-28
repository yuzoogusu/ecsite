from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=100)
    slug = models.SlugField() 
    dedcription = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title