from django.shortcuts import render, get_object_or_404
from .models import Project
import markdown2


def posts(request):
    projects = Project.objects.all().order_by("-id")
    return render(request, 'projects/posts.html', {"projects": projects})


def post(request, pk):
    project = get_object_or_404(Project, pk=pk)
    images = project.images.all()
    body = markdown2.markdown(project.text)
    return render(request, 'projects/post.html', {'project': project, "images": images, "body": body})

# Create your views here.
