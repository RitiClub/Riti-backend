from rest_framework import serializers
from .models import Customer, Category, Product, Orders, OrderItem

# Customer Serializer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_id', 'name', 'address', 'contact']

# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id', 'title', 'description', 'image']

# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    category_id = CategorySerializer()  # Nested serializer for Category

    class Meta:
        model = Product
        fields = ['product_id', 'title', 'description', 'image', 'caption', 'price', 'discount', 'category_id']

# OrderItem Serializer
class OrderItemSerializer(serializers.ModelSerializer):
    products_id = ProductSerializer()  # Nested serializer for Product

    class Meta:
        model = OrderItem
        fields = ['order_id', 'products_id', 'price', 'date']

# Orders Serializer
class OrdersSerializer(serializers.ModelSerializer):
    customer_id = CustomerSerializer()  # Nested serializer for Customer
    orderitem_set = OrderItemSerializer(many=True)  # Nested serializer for OrderItems

    class Meta:
        model = Orders
        fields = ['order_id', 'customer_id', 'order_date', 'total_price', 'orderitem_set']
