from django.db import models

# Creating the model class
class Product(models.Model):
    name = models.CharField(max_length=300, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='media')
    
    def __str__(self):
        return self.name