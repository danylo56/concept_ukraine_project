from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.title

    def short_text(self):
        md_chars = ['#', "*", "_", "[", "]", "(", ")"]
        return "".join(list(filter(lambda char: char if char not in md_chars else "", " ".join(self.text.split()[:15]))))


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="images")
# Create your models here.
