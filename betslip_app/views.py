from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from betslip_app.serializers import *
from betslip_app.models import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class BetSlipViewSet(viewsets.ModelViewSet):
	queryset = BetSlip.objects.all()
	serializer_class = BetSlipSerializer

class MatchViewSet(viewsets.ModelViewSet):
	queryset = Match.objects.all()
	serializer_class = MatchSerializer