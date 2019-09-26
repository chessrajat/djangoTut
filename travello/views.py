from django.shortcuts import render

# Create your views here.
from travello.models import Destination


def index(request):
    dest1 = Destination()
    dest1.name = "Mumbai"
    dest1.desc = "fast city"
    dest1.img = "destination_1.jpg"
    dest1.price = 800

    dest2 = Destination()
    dest2.name = "Mumbai"
    dest2.desc = "fast city"
    dest2.img = "destination_2.jpg"
    dest2.price = 801

    dest3 = Destination()
    dest3.name = "Mumbai"
    dest3.desc = "fast city"
    dest3.img = "destination_3.jpg"
    dest3.price = 802

    dests = [dest1, dest2, dest3]

    return render(request, "index.html", {"dests": dests})