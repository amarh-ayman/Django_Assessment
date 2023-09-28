from django.contrib import admin
from .models import CustomUser, Product, Transaction,TransactionItem

# add models to the Django administration
admin.site.register(CustomUser)
admin.site.register(Product)
admin.site.register(Transaction)
admin.site.register(TransactionItem)