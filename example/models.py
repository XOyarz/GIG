from django.db import models

# Create your models here.
#
class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    continent = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,)
    country_id = models.ForeignKey(Country, related_name='Company')

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    company_id = models.ForeignKey(Company)
    details = models.TextField(max_length=250, default='', blank=True)

    def __str__(self):
        return self.name


class CountryProducts(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, related_name='CountryProducts')
    country_id = models.ForeignKey(Country, related_name='CountryProducts')
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.product_id) +" " + str(self.country_id)




