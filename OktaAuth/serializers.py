from rest_framework import serializers


class UserDataLogInSerializer(serializers.Serializer):
    username = serializers.EmailField()
    password = serializers.CharField()
