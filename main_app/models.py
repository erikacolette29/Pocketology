from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

HOWTOXIC = (
    ('Baby Strength', 'Baby Strength'),
    ('Oh Boy', 'Oh Boy'),
    ('Deadly', 'Deadly')
)


class Toxic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    funfact = models.TextField(max_length=250)
    howtoxic = models.CharField(max_length=15,
        choices=HOWTOXIC,
        default=HOWTOXIC[0][0],
    
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'toxic_id': self.id})


class Rating(models.Model):
    comments = models.CharField(max_length=250)

    toxic = models.ForeignKey(Toxic, on_delete=models.CASCADE)

    def __str__(self):
     return self.comments



class Photo(models.Model):
    url = models.CharField(max_length=200)
    toxic = models.ForeignKey(Toxic, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for toxic_id: {self.toxic_id} @{self.url}"