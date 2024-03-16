from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from apps.models import User, Product


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ('groups', 'password',)


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = ()


class RegisterModelSerializer(ModelSerializer):
    confirm_password = CharField(write_only=True)
    username = CharField(max_length=255)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        confirm_password = data.pop('confirm_password')
        if confirm_password and confirm_password == data['password']:
            data['password'] = make_password(data['password'])
            return data
        raise ValidationError("Parol mos emas")


