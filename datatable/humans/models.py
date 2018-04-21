from django.db import models


class Human(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
