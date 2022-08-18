from csv import field_size_limit
from rest_framework import serializers
from endpoint.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        