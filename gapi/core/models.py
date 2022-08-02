from django.db import models

# Create your models here.

class Categoria(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name

class Producto(models.Model):
    name = models.CharField(max_length=155)
    price = models.IntegerField()
    category = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name