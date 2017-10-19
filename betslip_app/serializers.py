from django.contrib.auth.models import User, Group
from rest_framework import serializers
from betslip_app.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')

class MatchSerializer(serializers.ModelSerializer):
	class Meta:
		model = Match
		fields = ('id', 'name', 'market_name', 'bet', 'start_date', 'tournament_name', 'possibility')

class BetSlipSerializer(serializers.ModelSerializer):
	matches = MatchSerializer(many=True, read_only=True)

	class Meta:
		model = BetSlip
		fields = ('id', 'name', 'tournament_name', 'market_name', 'total_bet','start_date', 'matches')




