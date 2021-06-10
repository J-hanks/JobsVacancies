from django.db import models
from django.utils.translation import ugettext as _
from .TimeStampedModelMixin import TimeStampedModelMixin


class Company(TimeStampedModelMixin):
    name = models.CharField(_("Name"), max_length=255)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name
