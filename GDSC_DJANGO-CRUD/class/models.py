from django.db import models
from django.urls import reverse

# Create your models here.

class Dsc(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self) ->str:
        return self.name

    def get_absolute_url(self):
        return reverse('detailview', kwargs={"pk":self.pk})
