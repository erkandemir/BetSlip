from django.db import models
from django.contrib.auth.models import User,Group

class BetSlip(models.Model):
	name = models.CharField(max_length=100)
	tournament_name = models.CharField(max_length=100)
	market_name = models.CharField(max_length=100)
	total_bet = models.FloatField()		
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	is_active = models.BooleanField(default=False)
	matches = models.ManyToManyField("Match")

	def get_matches(self):
		return " |.| ".join([b.name for b in self.matches.all()])

class Match(models.Model):
	name = models.CharField(max_length=100)
	market_name = models.CharField(max_length=100)
	tournament_name = models.CharField(max_length=100)
	start_date = models.DateTimeField()
	bet = models.FloatField()	
	possibility = models.FloatField(null= True)	
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.name + " ' " + self.market_name + " ' " + str(self.bet)



