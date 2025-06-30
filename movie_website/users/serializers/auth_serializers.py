from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

from models.user import CustomerUser


__all__ = [
    'RegisterSerializer',
]

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_two = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomerUser
        fields = (
            'id', 'email', 'username', 
            'password', 'password_two', 'birthday',
            'bio', 'profile_image'
            )

    def validate(self, data):
        if data['password'] != data['password_two']:
            raise serializers.ValidationError('Passwords must match')
        return data
    
    def create(self, validated_data):
        validated_data.pop('password_two')
        user = CustomerUser.objects.create_user(
            email = validated_data['email'],
            username = validated_data['username'],
            password=validated_data['password']
        )
    
        user.birthday = validated_data.get('birthday')
        user.bio = validated_data.get('bio')
        user.profile_image = validated_data.get('profile_image')
        user.save()

        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        try:
            user = CustomerUser.objects.get(email=email)
        except CustomerUser.DoesNotExist:
            raise serializers.ValidationError({'email': 'There is no user with this email.'})
        
        if not user.check_password(password):
            raise serializers.ValidationError({'password': 'Wrong password'})
        
        data['user'] = user
        
        return data