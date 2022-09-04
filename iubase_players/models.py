from django.db import models
from django.utils.timezone import now


class Player(models.Model):
    first = models.CharField(null=False, max_length=100,)
    middle = models.CharField(blank=True, max_length=100,)
    last = models.CharField(null=False, max_length=100,)
    hometown = models.CharField(blank=True, max_length=100,)
    state = models.CharField(blank=True, max_length=100,)
    country = models.CharField(blank=True, max_length=100,)
    birthdate = models.DateField(blank=True, )
    height = models.FloatField(blank=True, )
    weight = models.FloatField(blank=True, )
    bats = models.CharField(blank=True, max_length=1,)
    throws = models.CharField(blank=True, max_length=1,)

    def __str__(self) -> str:
        return f"{self.first} {self.last}"


class Level(models.Model):
    description = models.CharField(null=False, max_length=100,)

    def __str__(self) -> str:
        return self.description


class League(models.Model):
    description = models.CharField(null=False, max_length=100,)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.description


class Team(models.Model):
    name = models.CharField(null=False, max_length=100,)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    city = models.CharField(null=False, max_length=100,)
    state = models.CharField(blank=True, max_length=100,)
    country = models.CharField(null=False, max_length=100,)

    def __str__(self) -> str:
        return self.name


class TransactionType(models.Model):
    description = models.CharField(null=False, max_length=100,)

    def __str__(self) -> str:
        return self.description


class Position(models.Model):
    description = models.CharField(null=False, max_length=100,)

    def __str__(self) -> str:
        return self.description


class Transaction(models.Model):
    date_announced = models.DateField(null=False, default=now)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, blank=True, on_delete=models.CASCADE)
    year = models.IntegerField(null=False)
    season = models.CharField(null=False, max_length=10,)
    jersey = models.IntegerField(null=True)
    position = models.ForeignKey(Position, blank=True, on_delete=models.CASCADE)
    trans_type = models.ForeignKey(TransactionType, on_delete=models.CASCADE)
    draft_round = models.IntegerField(null=True)
    pro_org = models.CharField(blank=True, max_length=100,)

    def __str__(self) -> str:
        return f"{self.date_announced}"


class Academic(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    school = models.ForeignKey(Team, on_delete=models.CASCADE)
    degree_date = models.DateField(blank=True, )
    degree_level = models.CharField(null=False, max_length=100,)
    major = models.CharField(null=False, max_length=100,)

    def __str__(self) -> str:
        return self.degree_level


class Article(models.Model):
    player = models.ManyToManyField(Player)
    title = models.CharField(null=False, max_length=100,)
    url = models.URLField(null=False)
    publication = models.CharField(null=False, max_length=100,)
    date = models.DateField(blank=True, )

    def __str__(self) -> str:
        return self.title


class Headshot(models.Model):
    player = models.ManyToManyField(Player)
    url = models.URLField(null=False)
    date = models.DateField(blank=True,)

    def __str__(self) -> str:
        return self.url


class Photo(models.Model):
    player = models.ManyToManyField(Player)
    url = models.URLField(null=False)
    date = models.DateField(default=now)
    description = models.CharField(null=False, max_length=100,)
    credit = models.CharField(null=False, max_length=100,)

    def __str__(self) -> str:
        return self.description


class Accolade(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    description = models.CharField(null=False, max_length=100,)
    organization = models.CharField(null=False, max_length=100,)
    year = models.IntegerField(null=False)
    season = models.CharField(null=False, max_length=10,)

    def __str__(self) -> str:
        return self.description


class SocialPlatform(models.Model):
    platform = models.CharField(null=False, max_length=100,)

    def __str__(self) -> str:
        return self.platform


class PlayerSocial(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    platform = models.ForeignKey(SocialPlatform, on_delete=models.CASCADE)
    url = models.URLField(null=False)
    handle = models.CharField(blank=True, max_length=100,)

    def __str__(self) -> str:
        return self.url


class TeamSocial(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    platform = models.ForeignKey(SocialPlatform, on_delete=models.CASCADE)
    url = models.URLField(null=False)
    handle = models.CharField(blank=True, max_length=100,)

    def __str__(self) -> str:
        return self.url

    





    

