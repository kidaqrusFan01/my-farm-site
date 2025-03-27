from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 255)
    image = models.ImageField(upload_to='img/', blank=True, null=True)


    def __str__(self):
        return self.name




class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)