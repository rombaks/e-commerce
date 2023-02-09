from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "_id",
            "name",
            "image",
            "description",
            "brand",
            "category",
            "price",
            "countInStock",
            "rating",
            "numReviews",
        )
