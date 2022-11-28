from django.db import models


class File(models.Model):
    type = models.CharField(max_length=1)
    date = models.CharField(max_length=8)
    valor = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=11)
    hour = models.CharField(max_length=6)
    owner = models.CharField(max_length=14)
    store_name = models.CharField(max_length=19)
