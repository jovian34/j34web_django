from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt

from .models import Transaction, Player


@xframe_options_exempt
def roster(request, season, year):
    transactions = Transaction.objects.filter
    context = {
        "item": item,
    }
    return render(request, "iubase_players/roster.html", context)
