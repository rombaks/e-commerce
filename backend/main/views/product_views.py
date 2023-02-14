from rest_framework.decorators import api_view
from rest_framework.response import Response

from main.models import Product
from main.serializers import ProductSerializer


@api_view(["GET"])
def get_products(request):
    products = Product.objects.all()
    serirializer = ProductSerializer(products, many=True)
    return Response(serirializer.data)


@api_view(["GET"])
def get_product(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)
