from django.conf.urls import url
from example import views

urlpatterns = [
    url(r'api/products/$', views.ProductList.as_view()),
    url(r'api/products/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),
    url(r'api/countries/$', views.CountryList.as_view()),
    url(r'api/countries/(?P<pk>[0-9]+)/$', views.CountryDetail.as_view()),

    url(r'api/products/(?P<product_id>[0-9]+)/countries/$', views.CountryProductList.as_view()),

]