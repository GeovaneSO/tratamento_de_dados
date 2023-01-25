from django.db import models

class FormModel(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField()
