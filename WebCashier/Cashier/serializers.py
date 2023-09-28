from rest_framework import serializers
from .models import Product, Transaction, TransactionItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class TransactionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionItem
        fields = ('id', 'product', 'quantity')
        
class TransactionSerializer(serializers.ModelSerializer): 
    items = TransactionItemSerializer(many=True, read_only=True)

    class Meta:
        model = Transaction
        fields = ('id', 'cashier', 'number_of_items', 'items', 'transaction_time')
        read_only_fields = ('id', 'cashier', 'transaction_time')     

class PaySerializer(serializers.Serializer):
    items = serializers.ListField(
        child=serializers.DictField(
            child=serializers.IntegerField(min_value=1),
            allow_empty=False
        ),
        allow_empty=False
    )
    
