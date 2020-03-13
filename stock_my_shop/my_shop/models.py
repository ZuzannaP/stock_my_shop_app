from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.FloatField()
    vat = models.FloatField(choices=[(0.23, "0.23"), (0.08, "0.08"), (0.05, "0.05"), (0, "0")])
    stock = models.IntegerField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
