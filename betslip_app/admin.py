from django.contrib import admin
from betslip_app.models import BetSlip, Match
from django.db import models

class BetSlipAdmin(admin.ModelAdmin):
	filter_horizontal = ('matches',)	
	list_display = ('name', 'market_name', 'start_date', 'get_matches')

admin.site.register(BetSlip, BetSlipAdmin)


class MatchAdmin(admin.ModelAdmin):	
	list_display = ('name', 'market_name', 'bet','start_date')

admin.site.register(Match, MatchAdmin)


