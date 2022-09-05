from django.db import models
from django.utils.timezone import now


class Player(models.Model):
    first = models.CharField(
        max_length=20,
    )
    middle = models.CharField(
        blank=True,
        max_length=20,
    )
    last = models.CharField(
        max_length=20,
    )
    hometown = models.CharField(
        blank=True,
        max_length=20,
    )
    state = models.CharField(
        blank=True,
        max_length=10,
    )
    country = models.CharField(
        blank=True,
        max_length=20,
    )
    birthdate = models.DateField(
        blank=True,
    )
    height = models.FloatField(
        blank=True,
    )
    weight = models.FloatField(
        blank=True,
    )
    bats = models.CharField(
        blank=True,
        max_length=1,
    )
    throws = models.CharField(
        blank=True,
        max_length=1,
    )

    def __str__(self) -> str:
        return f"{self.first} {self.last}"


class Level(models.Model):
    description = models.CharField(
        max_length=20,
    )

    def __str__(self) -> str:
        return self.description


class League(models.Model):
    description = models.CharField(
        max_length=30,
    )
    level = models.ForeignKey(Level, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.description


class Team(models.Model):
    name = models.CharField(
        max_length=30,
    )
    league = models.ForeignKey(League, blank=True, on_delete=models.CASCADE)
    city = models.CharField(
        blank=True,
        max_length=20,
    )
    state = models.CharField(
        blank=True,
        max_length=10,
    )
    country = models.CharField(
        max_length=20,
    )

    def __str__(self) -> str:
        return self.name


class TransactionType(models.Model):
    description = models.CharField(
        max_length=30,
    )

    def __str__(self) -> str:
        return self.description


class Position(models.Model):
    description = models.CharField(
        max_length=10,
    )

    def __str__(self) -> str:
        return self.description


class Season(models.Model):
    description = models.CharField(
        max_length=10,
    )

    def __str__(self) -> str:
        return self.description


class Transaction(models.Model):
    date_announced = models.DateField(blank=False, default=now)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, blank=True, on_delete=models.CASCADE)
    year = models.IntegerField(blank=False)
    season = models.CharField(
        max_length=10,
    )
    jersey = models.IntegerField(blank=True, null=True, default=None)
    position = models.ForeignKey(Position, blank=True, on_delete=models.CASCADE)
    trans_type = models.ForeignKey(TransactionType, on_delete=models.CASCADE)
    draft_round = models.IntegerField(blank=True, null=True, default=None)
    pro_org = models.CharField(
        blank=True,
        max_length=30,
    )

    def __str__(self) -> str:
        return f"{self.date_announced}"


class Academic(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    school = models.ForeignKey(Team, on_delete=models.CASCADE)
    degree_date = models.DateField(
        blank=True,
    )
    degree_level = models.CharField(
        max_length=20,
    )
    major = models.CharField(
        blank=True,
        max_length=30,
    )

    def __str__(self) -> str:
        return self.degree_level


class Article(models.Model):
    player = models.ManyToManyField(Player)
    title = models.CharField(
        blank=False,
        max_length=100,
    )
    url = models.URLField(blank=False)
    publication = models.CharField(
        blank=True,
        max_length=30,
    )
    date = models.DateField(default=now)

    def __str__(self) -> str:
        return self.title


class Headshot(models.Model):
    player = models.ManyToManyField(Player)
    url = models.URLField(blank=False)
    date = models.DateField(
        blank=True,
    )

    def __str__(self) -> str:
        return self.url


class Photo(models.Model):
    player = models.ManyToManyField(Player)
    url = models.URLField(max_length=100)
    date = models.DateField(default=now)
    description = models.CharField(
        blank=True,
        max_length=50,
    )
    credit = models.CharField(
        null=False,
        max_length=30,
    )

    def __str__(self) -> str:
        return self.description


class Accolade(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    description = models.CharField(
        blank=False,
        max_length=100,
    )
    organization = models.CharField(
        blank=False,
        max_length=30,
    )
    year = models.IntegerField(blank=False, default=now)
    season = models.CharField(
        null=False,
        max_length=10,
    )

    def __str__(self) -> str:
        return self.description


class SocialPlatform(models.Model):
    platform = models.CharField(
        max_length=100,
    )

    def __str__(self) -> str:
        return self.platform


class PlayerSocial(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    platform = models.ForeignKey(SocialPlatform, on_delete=models.CASCADE)
    url = models.URLField(max_length=100)
    handle = models.CharField(
        blank=True,
        max_length=100,
    )

    def __str__(self) -> str:
        return self.url


class TeamSocial(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    platform = models.ForeignKey(SocialPlatform, on_delete=models.CASCADE)
    url = models.URLField(max_length=100)
    handle = models.CharField(
        blank=True,
        max_length=100,
    )

    def __str__(self) -> str:
        return self.url
