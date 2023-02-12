from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Product, User
from .serializers import ProductSerializer, UserSerializer, UserSerializerWithToken


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, user):
        data = super().validate(user)

        serializer = UserSerializerWithToken(self.user).data
        data.update(serializer)

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user(request):
    user = request.user
    serirializer = UserSerializer(user, many=False)
    return Response(serirializer.data)


@api_view(["GET"])
@permission_classes([IsAdminUser])
def get_users(request):
    users = User.objects.all()
    serirializer = UserSerializer(users, many=True)
    return Response(serirializer.data)


@api_view(["GET"])
def get_routes(request):
    routes = ["api/products", "and_so_on", "OpenAPI"]
    return Response(routes)


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
