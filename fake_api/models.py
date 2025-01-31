from django.db import models

# Create your models here.

class Productos(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    is_default = models.BooleanField(default=False, editable=False)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name