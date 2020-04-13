from django.db import models

# Create your models here.

property_type = (
    ('S',"Sale"),
    ('R',"Rent")
)

class Property(models.Model):
    name = models.CharField(max_length=50)
    #location
    property_type = models.CharField(choices=property_type, max_length=10)
    price = models.PositiveIntegerField()
    category = models.ForeignKey('Category',null = True, on_delete=models.SET_NULL)
    area = models.DecimalField(decimal_places=2, max_digits=8)
    beds_number = models.PositiveIntegerField()
    baths_number = models.PositiveIntegerField()
    garages_number = models.PositiveIntegerField()
    images = models.ImageField(upload_to='property/', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
                                                                        