from django.db import models

class Mystickynote(models. Model):
    name = models.CharField(max_length=50)
    set = models. SmallIntegerField()
    description = models.Textfield()
    created_by= models.CharField(maxlength=30)