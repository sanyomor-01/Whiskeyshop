from django.db import models

# Create your models here.
class ProductCategories(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering =('name',)
        verbose_name_plural = 'ProductCategories'

    def __str__(self):
        return self.name