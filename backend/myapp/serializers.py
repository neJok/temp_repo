from .models import WithdrawalRequest, Partner, CompanyBalance
from .models import Lead
from .models import Profile
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers

class ResponseSerializer(serializers.Serializer):
    user_name = serializers.CharField(max_length=100)
    user_id = serializers.CharField(max_length=100)
    message = serializers.CharField()

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        # Проверяем, существует ли пользователь с таким email
        user = User.objects.filter(email=data['email']).first()
        if not user:
            raise serializers.ValidationError("Пользователь с таким email не найден.")

        user = authenticate(username=user.username, password=data['password'])
        if not user:
            raise serializers.ValidationError("Неверный пароль.")

        return user


class RegisterSerializer(serializers.Serializer):
    company_name = serializers.CharField()
    telegram = serializers.CharField()
    company_link = serializers.URLField()
    recvisity = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate_email(self, value):
        # Проверяем, существует ли пользователь с таким email
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Пользователь с таким email уже существует.")
        return value

    def create(self, validated_data):
        # Создаем пользователя
        user = User.objects.create_user(
            username=validated_data['email'],  # Используем email как username
            email=validated_data['email'],
            password=validated_data['password']
        )
        # Создаем профиль и связываем его с пользователем
        profile = Profile.objects.create(
            user=user,
            company_name=validated_data['company_name'],
            telegram=validated_data['telegram'],
            company_link=validated_data['company_link'],
            recvisity=validated_data['recvisity']
        )
        return profile


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ('user', 'first_name', 'last_name', 'email', 'phone')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(
            username=user_data['username'],
            password=user_data['password'],
            email=user_data.get('email', '')
        )
        profile = Profile.objects.create(user=user, **validated_data)
        return profile


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'


class CompanyBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyBalance
        fields = '__all__'


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'


class WithdrawalRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = WithdrawalRequest
        fields = '__all__'
