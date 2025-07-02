from rest_framework import serializers
from .models import (
    Table, Ingredient,
    MenuItem, MenuItemIngredient,
    Order, OrderItem
)

# Stol serializer
class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'

# Ingredient serializer (ombor mahsulotlari)
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

# MenuItemIngredient — taomda qanday ingredient bor
class MenuItemIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(read_only=True)
    ingredient_id = serializers.PrimaryKeyRelatedField(
        queryset=Ingredient.objects.all(), source='ingredient', write_only=True
    )

    class Meta:
        model = MenuItemIngredient
        fields = ['id', 'ingredient', 'ingredient_id', 'amount_needed']

# MenuItem (taom) serializer
class MenuItemSerializer(serializers.ModelSerializer):
    ingredients_detail = MenuItemIngredientSerializer(
        source='menuitemingredient_set', many=True, read_only=True
    )

    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'price', 'ingredients_detail']

# OrderItem serializer — buyurtmadagi mahsulotlar
class OrderItemSerializer(serializers.ModelSerializer):
    menu_item_name = serializers.CharField(source='menu_item.name', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'menu_item', 'menu_item_name', 'quantity']

# Order serializer — asosiy buyurtma
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    table_number = serializers.IntegerField(source='table.number', read_only=True)
    waiter_username = serializers.CharField(source='waiter.username', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'table', 'table_number', 'waiter', 'waiter_username', 'status', 'created_at', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item in items_data:
            OrderItem.objects.create(order=order, **item)

        return order

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if items_data:
            instance.items.all().delete()
            for item in items_data:
                OrderItem.objects.create(order=instance, **item)

        return instance
