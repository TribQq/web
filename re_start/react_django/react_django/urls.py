from django.contrib import admin
from django.urls import path

from customers import views
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/customers/$', views.view_customers_list), # r'' for \ => \\ (auto-shielding(экранирование)
    url(r'^api/customers/(?P<pk>[0-9]+$', views.view_customers_detail),

]
