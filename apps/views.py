from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.models import User, Product
from apps.serializers import ProductModelSerializer, UserModelSerializer, \
    RegisterModelSerializer


class RegisterCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterModelSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()

    # filter_backends = (SearchFilter)

    @action(detail=False, methods=['GET'], url_path='get-me')
    def get_me(self, request, pk=None):
        if request.user.is_authenticated:
            return Response({'message': f'{request.user.username}'})
        return Response({'message': 'login qilinmagan'})


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    search_fields = ('name', 'description',)


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    http_method_names = ['put', 'delete', 'patch']
