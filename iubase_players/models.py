from django.db import models
from django.utils.timezone import now


class Player(models.Model):
    first = models.CharField(null=False, max_length=100,)
    middle = models.CharField(null=True, max_length=100,)
    last = models.CharField(null=False, max_length=100,)
    hometown = models.CharField(null=True, max_length=100,)
    state = models.CharField(null=True, max_length=100,)
    country = models.CharField(null=True, max_length=100,)
    birthdate = models.DateField(null=True, )
    height = models.FloatField(null=True, )
    weight = models.FloatField(null=True, )
    bats = models.CharField(null=True, max_length=1,)
    throws = models.CharField(null=True, max_length=1,)


class Level(models.Model):
    description = models.CharField(null=False, max_length=100,)


class League(models.Model):
    description = models.CharField(null=False, max_length=100,)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)


class Team(models.Model):
    name = models.CharField(null=False, max_length=100,)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    city = models.CharField(null=False, max_length=100,)
    state = models.CharField(null=True, max_length=100,)
    country = models.CharField(null=False, max_length=100,)


class TransactionType(models.Model):
    description = models.CharField(null=False, max_length=100,)


class Position(models.Model):
    description = models.CharField(null=False, max_length=100,)


class Transaction(models.Model):
    date_announced = models.DateField(null=False, default=now)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
    year = models.IntegerField(null=False)
    season = models.CharField(null=False, max_length=10,)
    jersey = models.IntegerField(null=True, )
    position = models.ForeignKey(Position, null=True, on_delete=models.CASCADE)
    trans_type = models.ForeignKey(TransactionType, on_delete=models.CASCADE)
    draft_round = models.IntegerField(null=True, )
    pro_org = models.CharField(null=False, max_length=100,)


class Academic(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    school = models.ForeignKey(Team, on_delete=models.CASCADE)
    degree_date = models.DateField(null=True, )
    degree_level = models.CharField(null=False, max_length=100,)
    major = models.CharField(null=False, max_length=100,)

class Article(models.Model):
    player = models.ManyToManyField(Player)
    title = models.CharField(null=False, max_length=100,)
    url = models.URLField(null=False)
    publication = models.CharField(null=False, max_length=100,)
    date = models.DateField(null=True, )


class Headshot(models.Model):
    player = models.ManyToManyField(Player)
    url = models.URLField(null=False)
    date = models.DateField(null=True,)

class Photo(models.Model):
    player = models.ManyToManyField(Player)
    url = models.URLField(null=False)
    date = models.DateField(default=now)
    description = models.CharField(null=False, max_length=100,)
    credit = models.CharField(null=False, max_length=100,)


class Accolade(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    description = models.CharField(null=False, max_length=100,)
    organization = models.CharField(null=False, max_length=100,)
    year = models.IntegerField(null=False)
    season = models.CharField(null=False, max_length=10,)



class SocialPlatform(models.Model):
    platform = models.CharField(null=False, max_length=100,)


class PlayerSocial(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    platform = models.ForeignKey(SocialPlatform, on_delete=models.CASCADE)
    url = models.URLField(null=False)
    handle = models.CharField(null=True, max_length=100,)


class TeamSocial(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    platform = models.ForeignKey(SocialPlatform, on_delete=models.CASCADE)
    url = models.URLField(null=False)
    handle = models.CharField(null=True, max_length=100,)

    





    

