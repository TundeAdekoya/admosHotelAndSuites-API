from rest_framework import serializers
from django.contrib.auth.models import User 
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=False)
    _id = serializers.SerializerMethodField(read_only=False)
    isAdmin = serializers.SerializerMethodField(read_only=False)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin']

    def get__id(self, obj):
        return obj.id

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email

        return name


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

class Room_serviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room_service
        fields = '__all__'

class Event_serviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event_service
        fields = '__all__'