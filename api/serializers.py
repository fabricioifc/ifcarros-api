from rest_framework import serializers
from api.models import User, UserProfile, Car
from django.contrib.auth.models import Group


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('dtnascimento', 'endereco', 'cidade', 'cep', 'avatar')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Bifrost user writable nested serializer
    """
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('url', 'email', 'username', 'name', 'siape', 'password', 'profile', 'groups')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        # profile.title = profile_data.get('title', profile.title)
        profile.dtnascimento = profile_data.get(
            'dtnascimento', profile.dtnascimento)
        profile.endereco = profile_data.get('endereco', profile.endereco)
        # profile.country = profile_data.get('country', profile.country)
        profile.cidade = profile_data.get('cidade', profile.cidade)
        profile.cep = profile_data.get('cep', profile.cep)
        profile.avatar = profile_data.get('avatar', profile.avatar)
        profile.save()

        return instance


class CarSerializer(serializers.HyperlinkedModelSerializer):
    """
    Bifrost user writable nested serializer
    """
    class Meta:
        model = Car
        # fields = ('marca', 'modelo', 'ano', 'km', 'descricao')
        fields = '__all__'
        # exclude = ('user',)

    def create(self, validated_data):
        car = Car(**validated_data)
        car.save()
        # UserProfile.objects.create(user=user, **profile_data)
        return car

    def update(self, instance, validated_data):
        instance.marca = validated_data.get('marca', instance.marca)
        instance.modelo = validated_data.get('modelo', instance.modelo)
        instance.ano = validated_data.get('ano', instance.ano)
        instance.km = validated_data.get('km', instance.km)
        instance.descricao = validated_data.get(
            'descricao', instance.descricao)

        if self.is_valid():
            instance.save()

        return instance
