from django.conf.urls import url, include
from . import views

urlpatterns=[
url(r'^bevendor$',views.bevendor),
url(r'^fooddel$',views.fooddel),
url(r'^contact$',views.contact),
url(r'^index$',views.index),]