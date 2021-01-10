from django.shortcuts import render
from .models import Event


def all_events(request):
    events = Event.objects.all().order_by("-date")
    data = []
    for elem in enumerate(events):
        data.append({"bool": elem[0] % 2 == 0, "event": elem[1]})

    return render(request, "events/events.html", {"data": data})
# Create your views here.
