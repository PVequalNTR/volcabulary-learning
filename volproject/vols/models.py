from django.db import models
from django.contrib.postgres.fields import ArrayField

class Latest_categories(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    vol_list = ArrayField(models.CharField(max_length=100))
    date_added = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ('-date_added', )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'{self.slug}/'

class Sentence(models.Model):
    name = models.CharField(max_length=100)
    word = models.CharField(max_length=100)
    source = models.CharField(max_length=100)

    class Meta:
        ordering = ('word', )

    def __str__(self):
        return self.name
