from example.models import Product, Country
from example.serializers import ProductSerializer, CountrySerializer
from rest_framework import generics



class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Product.objects.all()
        company = self.request.query_params.get('company', None)
        if company is not None:
            queryset = queryset.filter(company_id=company)
        return queryset


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Country.objects.all()
        company = self.request.query_params.get('company', None)
        if company is not None:
            queryset = queryset.filter(Company=company)
        return queryset

class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryProductList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get_queryset(self):

        product_id = self.kwargs['product_id']

        return Country.objects.filter(CountryProducts=product_id)
