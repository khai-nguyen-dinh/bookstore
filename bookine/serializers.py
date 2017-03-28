from rest_framework import serializers

from bookine.models import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'book_name',
                  'price', 'thumbnail',
                  'description', 'author')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',
                  'password', 'name',
                  'email', 'sdt',
                  'address','book')


class UserSigninSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',
                  'password')



class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('user', 'book', 'count', 'no', 'is_payment')


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('cart', 'delivery')
