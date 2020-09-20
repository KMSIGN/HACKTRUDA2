from django.db import models
from six import text_type

# Create your models here.
class Person(models.Model):
    name = models.URLField(max_length=130,verbose_name=u"URL", blank=True)
    file = models.FileField(blank=True)