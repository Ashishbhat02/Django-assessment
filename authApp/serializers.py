from .models import User_new
# from rest_framework import ap
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_new
        fields = ('id' ,'full_name', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_new
        fields = ('id' ,'full_name', 'email' , 'password')

    def createUser(self, validated_data):
        user = User_new.objects.create_user(
            full_name = validated_data["full_name"],
            email = validated_data["email"],
            password = validated_data["password"]
        )
        return user
    
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(required = True)
    password = serializers.CharField(required = True)