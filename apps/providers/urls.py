from django.contrib import admin
from django.urls import path
from .views import (
    ProvidersList, 
    ProviderDetail, 
    ProviderList, 
    PolygonDetail, 
    PolygonList, 
    ZoneList
)

urlpatterns = [
    path('providers', ProvidersList.as_view()),
    path('provider/new', ProviderList.as_view()),
    path('provider/<int:pk>/', ProviderDetail.as_view()),

    path('zone/new', PolygonList.as_view()),
    path('zone/<int:pk>/', PolygonDetail.as_view()),

    path('zone/', ZoneList.as_view()),
]