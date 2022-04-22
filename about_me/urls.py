from unicodedata import name
from django.urls import path

from .views import *

app_name = 'about_me'
urlpatterns = [
   path('', about_main, name='about_main'),
   path('alt/', alt_about_me, name='alt_about_me'),
   
   
   path('portfolio/', portfolio_main, name='portfolio_main'),
   path('portfolio/aeropack', aeropack, name='aeropack_box'),
   
   path('portfolio/alapantan', alapantan, name='alapantan'),
   path('portfolio/alapantan/basket', alapantan_basket, name='alapantan_basket'),
   path('portfolio/alapantan/buy', alapantan_buy, name='alapantan_buy'),
   path('portfolio/alapantan/card', alapantan_card, name='alapantan_card'),
   path('portfolio/alapantan/catalog', alapantan_catalog, name='alapantan_catalog'),
   path('portfolio/alapantan/checkout', alapantan_checkout, name='alapantan_checkout'),
   path('portfolio/alapantan/checkout/1', alapantan_checkout_1, name='alapantan_checkout_1'),
   path('portfolio/alapantan/checkout/2', alapantan_checkout_2, name='alapantan_checkout_2'),
   path('portfolio/alapantan/checkout/3', alapantan_checkout_3, name='alapantan_checkout_3'),
   path('portfolio/alapantan/checkout/4', alapantan_checkout_4, name='alapantan_checkout_4'),
   path('portfolio/alapantan/checkout/5', alapantan_checkout_5, name='alapantan_checkout_5'),
   path('portfolio/alapantan/delivery', alapantan_delivery, name='alapantan_delivery'),
   path('portfolio/alapantan/loyality', alapantan_loyality, name='alapantan_loyality'),
   path('portfolio/alapantan/modals', alapantan_modals, name='alapantan_modals'),
   path('portfolio/alapantan/news', alapantan_news, name='alapantan_news'),
   path('portfolio/alapantan/payment', alapantan_payment, name='alapantan_payment'),
   path('portfolio/alapantan/personal_area', alapantan_personal_area, name='alapantan_personal_area'),
   path('portfolio/alapantan/question', alapantan_question, name='alapantan_question'),

   path('portfolio/photo_birds', photo_birds, name='photo_birds'),


   # path('404/', handler_404, name='handler_404'), #alternate handler
]