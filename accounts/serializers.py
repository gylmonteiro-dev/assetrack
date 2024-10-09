from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile


class UserModelSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    

    class Meta:
        model = User
        fields = ['id', 'username', 'password']


    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        return user

    
    def validate(self, values):

        confirm_password = self.context['request'].data.get('confirm_password')
        if not confirm_password:
            raise serializers.ValidationError("O campo confirm_password é obrigatório")

        if values['password'] != confirm_password:
            raise serializers.ValidationError("As senhas não coincidem") 
        return values


class UserProfileSerializar(serializers.ModelSerializer):
    user = UserModelSerializer()

    class Meta:
        model = UserProfile
        fields = (["id", "user", "person_registration_number", "organization"])
