from django.db import models
from django.urls import reverse
# Create your models here.

HOWTOXIC = (
    ('B', 'Baby Strength'),
    ('M', 'Oh Boy'),
    ('D', 'Deadly')
)


class Toxic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    funfact = models.TextField(max_length=250)
    howtoxic = models.CharField(max_length=1,
        choices=HOWTOXIC,
        default=HOWTOXIC[0][0]
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'toxic_id': self.id})

