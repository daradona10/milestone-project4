from django.conf.urls import url, include
from .views import all_products, all_jerseys, all_shorts, all_socks, all_base_layers, all_footballs


urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^jerseys/$', all_jerseys, name='products'),
    url(r'^shorts/$', all_shorts, name='products'),
    url(r'^socks/$', all_socks, name='products'),
    url(r'^base_layers/$', all_base_layers, name='products'),
    url(r'^footballs/$', all_footballs, name='products'),
]