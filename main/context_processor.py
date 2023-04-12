from .models import *


def menu_categories(request):
    categories = SubCategory.objects.all().order_by('id')
    locations = City.objects.all()
    states = State.objects.all()
    return {'categories': categories,'locations':locations,'states':states}