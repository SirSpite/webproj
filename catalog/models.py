from django.db import models

class Product(models.Model):
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    text = models.TextField()
    price = models.FloatField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
