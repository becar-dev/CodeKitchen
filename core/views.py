from rest_framework import viewsets
from .models import (
    Table, Ingredient,
    MenuItem, MenuItemIngredient,
    Order, OrderItem
)
from .serializers import (
    TableSerializer, IngredientSerializer,
    MenuItemSerializer, MenuItemIngredientSerializer,
    OrderSerializer, OrderItemSerializer
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Sum

# 🪑 Stol View
class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticated]


# 🧂 Ingredient (ombor) View
class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


# 🍽️ MenuItem View
class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer





# 🔗 MenuItemIngredient View (admin uchun)
class MenuItemIngredientViewSet(viewsets.ModelViewSet):
    queryset = MenuItemIngredient.objects.all()
    serializer_class = MenuItemIngredientSerializer


# 🧾 Order View
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().select_related('table', 'waiter').prefetch_related('items')
    serializer_class = OrderSerializer


    def perform_create(self, serializer):
        serializer.save(waiter=self.request.user)  # Ofitsiant — hozirgi foydalanuvchi

    def perform_update(self, serializer):
        order = serializer.save()
        # Agar status "done" bo‘lsa — ingredientlarni kamaytiramiz
        if order.status == 'done':
            for item in order.items.all():
                for ing in item.menu_item.ingredients.through.objects.filter(menu_item=item.menu_item):
                    ing_obj = ing.ingredient
                    ing_obj.quantity -= ing.amount_needed * item.quantity
                    ing_obj.save()
