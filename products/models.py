from django.db import models
from django.utils import timezone

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100)
    cost = models.FloatField()
    img = models.ImageField(upload_to='pics', null=True)
    description = models.TextField(max_length=500)
    created_on = models.DateTimeField(default = timezone.now)#auto_now_add=True) #auto_now_add field is saved as the current timestamp when a row is first added
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True) #auto_now fields are updated to the current timestamp every time an object is saved
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Products'
        # Add verbose name
        verbose_name = 'Products List'


