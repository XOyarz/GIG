from django.contrib import admin
from django.utils.html import linebreaks

from .models import Country, Product, Company, CountryProducts


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','company_id', 'country_availability', 'country_price', )

    # I wasn't sure if you wanted just the country, or just the stock availability, so I left both in.
    def country_availability(self, product):
        return [linebreaks((str(i.country_id) + ' = '+ str(i.stock)))  for i in product.CountryProducts.all()]
    country_availability.allow_tags = True

    def country_price(self, prod):
        return [linebreaks(i.price) for i in prod.CountryProducts.all()]
    country_price.allow_tags = True

admin.site.register(Country)
admin.site.register(Company)
admin.site.register(CountryProducts)

