from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to="img/")
    
    def __str__(self):
        return self.name