from django.contrib import admin

from .models import (
    Player,
    League,
    Level,
    Team,
    Season,
    Transaction,
    Position,
    TransactionType,
    Academic,
    Article,
    Headshot,
    Photo,
    PlayerSocial,
    SocialPlatform,
    TeamSocial,
)


admin.site.register(Player)
admin.site.register(League)
admin.site.register(Level)
admin.site.register(Team)
admin.site.register(Season)
admin.site.register(Transaction)
admin.site.register(Position)
admin.site.register(TransactionType)
admin.site.register(Academic)
admin.site.register(Article)
admin.site.register(Headshot)
admin.site.register(Photo)
admin.site.register(PlayerSocial)
admin.site.register(SocialPlatform)
admin.site.register(TeamSocial)
