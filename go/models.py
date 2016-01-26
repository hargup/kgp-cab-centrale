from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class journey(models.Model):
    traveller_name = models.CharField(null=False, blank=False, unique=False,
                                      max_length=100)
    traveller_email = models.EmailField(null=False, blank=False, unique=False)
    traveller_phone = models.IntegerField(null=False, blank=False, unique=False)
    start_time = models.DateTimeField(null=False, blank=False)
    end_time = models.DateTimeField(null=False, blank=False)

    def __str__(self):
    	return " ".join([traveller_name, start_time, end_time])
