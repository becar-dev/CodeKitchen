from django.db import models
from django.contrib.auth.models import User

# Stol raqami (ofitsiant buyurtma oladi)
class Table(models.Model):
    number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"Table {self.number}"

# Ombordagi mahsulotlar (ingredientlar)
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()  # kg, litr, dona

    def __str__(self):
        return self.name

# Menyudagi har bir taom
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    ingredients = models.ManyToManyField(Ingredient, through='MenuItemIngredient')

    def __str__(self):
        return self.name

# Taom uchun ingredient miqdori
class MenuItemIngredient(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount_needed = models.FloatField()  # 1 ta taom uchun qancha kerak

# Buyurtma (ofitsiant tomonidan kiritiladi)
class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),  # ⬅️ yangi qo‘shilgan status
        ('pending', 'Pending'),
        ('cooking', 'Cooking'),
        ('done', 'Done'),
    ]

    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    waiter = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.status}"

# Buyurtmadagi mahsulotlar
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name}"
