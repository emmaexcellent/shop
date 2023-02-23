from .models import *


def menu_categories(request):
    categories = Category.objects.all()
    locations = City.objects.all()
    states = State.objects.all()
    return {'categories': categories,'locations':locations,'states':states}