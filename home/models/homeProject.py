from django.db import models
from .skills import Skill

class HomeProject(models.Model):
    image = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.CharField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, related_name='projects')
    githubLink = models.CharField(max_length=100, blank=True, null=True)
    show_on_homepage = models.BooleanField(default=False)


    def __str__(self):
        return self.title
