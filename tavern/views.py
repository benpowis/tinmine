from django.shortcuts import render

from .models import Drink
from .models import Status

# Create your views here.
def index(request):
    served_drinks = Drink.objects.order_by('strength')
    status = Status.objects.all().first()
    context = {'served_drinks': served_drinks, 'status': status}
    return render(request, 'tavern/index.html', context)

def shop(request):
    status = Status.objects.all().first()
    context = {'status': status}
    return render(request, 'tavern/shop.html', context)

def fight(request):
    status = Status.objects.all().first()
    context = {'status': status}
    return render(request, 'tavern/fight.html', context)
