from django.db import models

class Resume(models.Model):
    file =models.URLField(blank=True, null=True)

    def __str__(self):
        return self.file.name