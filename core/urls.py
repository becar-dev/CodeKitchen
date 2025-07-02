from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TableViewSet,
    IngredientViewSet,
    MenuItemViewSet,
    MenuItemIngredientViewSet,
    OrderViewSet
)

router = DefaultRouter()
router.register(r'tables', TableViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'menu-items', MenuItemViewSet)
router.register(r'menu-item-ingredients', MenuItemIngredientViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
