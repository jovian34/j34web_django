from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to jovian34 LLC")
