from django.db import models


class Cnab(models.Model):
    title = models.CharField(max_length=30)
    file = models.FileField(upload_to="documents/")

    def __str__(self):
        return self.title
