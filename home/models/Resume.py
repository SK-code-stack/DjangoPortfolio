from django.db import models

class Resume(models.Model):
    file =models.FileField(upload_to="resume/")

    def __str__(self):
        return self.file.name