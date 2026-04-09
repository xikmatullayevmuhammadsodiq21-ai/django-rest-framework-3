from django.db import models

# Create your models here.


class Telefon(models.Model):
    name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.name}"