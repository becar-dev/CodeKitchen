from django.contrib import admin
from .models import (
    Table, Ingredient,
    MenuItem, MenuItemIngredient,
    Order, OrderItem
)

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['number', 'capacity']
    search_fields = ['number']

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity']
    search_fields = ['name']

class MenuItemIngredientInline(admin.TabularInline):
    model = MenuItemIngredient
    extra = 1

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name']
    inlines = [MenuItemIngredientInline]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'table', 'waiter', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['waiter__username']
    date_hierarchy = 'created_at'

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'menu_item', 'quantity']
