from django.contrib import admin
from django.urls import path, include
from lavajato.views import ClientesViewSet, VeiculosViewSets
from rest_framework import routers


router = routers.DefaultRouter()
router.register('clientes', ClientesViewSet)
router.register('veiculos', VeiculosViewSets)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
