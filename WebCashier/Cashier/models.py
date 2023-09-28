from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User Model
class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100)
    last_login = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.full_name

# Product Model
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name

# Transaction Model
class Transaction(models.Model):
    cashier = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    number_of_items = models.PositiveIntegerField()
    items = models.ManyToManyField(Product, through='TransactionItem')
    transaction_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.pk} by {self.cashier.full_name} at {self.transaction_time}"

# Transaction Item Model
class TransactionItem(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} x{self.quantity} in Transaction {self.transaction.pk}"
