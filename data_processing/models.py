from django.db import models


class Process(models.Model):
    transaction_type = models.IntegerField()
    transaction_date = models.DateField()
    transaction_value = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    transaction_hour = models.TimeField()
    store_owner = models.CharField(max_length=50)
    store_name = models.CharField(max_length=50)
