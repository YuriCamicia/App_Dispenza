from django.contrib.auth.models import User, Group
from rest_framework import serializers

from api_app.api.models import Prodotto_Dispensa, Spesa, Prodotto_Spesa


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email','url')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ProdottoDispensaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prodotto_Dispensa
        fields = ('id','nome', 'scadenza','quantità')

class ProdottoSpesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prodotto_Spesa
        fields = ('id','nome', 'prezzo','quantità')


class SpesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spesa
        fields = ('id', 'titolo', 'prezzo_tot', 'prodotto')