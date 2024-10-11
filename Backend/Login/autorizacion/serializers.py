from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']  # Ajusta los campos según lo que necesites
        extra_kwargs = {'password': {'write_only': True}}

