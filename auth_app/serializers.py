from .models import User
from rest_framework.serializers import ModelSerializer


class SignUpSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'bin', 'role']

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'bin', 'role']


class ProfileUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

