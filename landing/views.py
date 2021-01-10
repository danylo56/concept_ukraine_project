from django.shortcuts import render
from projects.models import Project
from events.models import Event


def index(request):
    last_projects = Project.objects.all().order_by("-id")[:3]
    last_events = Event.objects.all().order_by("-date")[:3]
    data = []
    for elem in enumerate(last_events):
        data.append({"bool": elem[0] % 2 == 0, "event": elem[1]})
    return render(request, 'landing/index.html', {'posts': last_projects, "data": data})
# Create your views here.
