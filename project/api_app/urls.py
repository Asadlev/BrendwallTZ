from django.urls import path
from .views import ProductAPIView, products_page


urlpatterns = [
    path('', products_page, name='products_page'),
    path('api/products/', ProductAPIView.as_view(), name='products_api'),

]



