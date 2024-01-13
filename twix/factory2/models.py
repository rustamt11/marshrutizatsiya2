from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    creation_date = models.DateField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.name
