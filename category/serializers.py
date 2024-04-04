from rest_framework import serializers
from category.models import Category


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class CategorySerializer(serializers.ModelSerializer):
    parent_name = serializers.ReadOnlyField(source='parent.name')
    children = CategoryListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'

