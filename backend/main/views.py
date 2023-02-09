from rest_framework.decorators import api_view
from rest_framework.response import Response

from main.products import products


@api_view(["GET"])
def get_routes(request):
    routes = ["api/products", "and_so_on", "OpenAPI"]
    return Response(routes)


@api_view(["GET"])
def get_products(request):
    return Response(products)


@api_view(["GET"])
def get_product(request, pk):
    product = None
    for prod in products:
        if prod["_id"] == pk:
            product = prod
            break

    return Response(product)
