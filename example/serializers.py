from rest_framework import serializers
from .models import Product, Country, Company, CountryProducts

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'company_id', 'details')

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name', 'continent')

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'country_id')


class CountryProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryProducts
        fields = ('id', 'product_id', 'country_id', 'stock', 'price')