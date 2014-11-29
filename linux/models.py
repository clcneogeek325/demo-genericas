from django.db import models
from django.core.urlresolvers import reverse

class Distro(models.Model):
    nombre = models.CharField(max_length=100)

    #def __unicode__(self):
     #   return self.nombre
    def get_absolute_url(self):
        return reverse('distro-detail', kwargs={'pk': self.pk})
