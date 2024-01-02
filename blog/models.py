from django.db import models
from django.urls import reverse
# Create your models here.
class FarmerHome(models.Model):
    name = models.CharField(max_length=300)
    desigination = models.CharField(max_length=300)
    img = models.ImageField(upload_to='farmer/img')
    slug = models.SlugField(max_length=300)
    def get_absolute_url(self):
        return reverse('farmersDetail', args=[self.slug])

    def __str__(self):
        return self.name

