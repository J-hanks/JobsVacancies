from django.db import models

class TimeStampedModelMixin(models.Model):

    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
       abstract = True
