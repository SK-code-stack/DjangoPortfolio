from django.db import models

class Intro(models.Model):
    selfIntroTitle = models.CharField(max_length=100 , blank=False, null=False )
    selfIntro = models.CharField( blank=False, null=False)
    EducationTitle = models.CharField(max_length=100, blank=False, null=False)
    Education = models.CharField( blank=False, null=False)
    LanguagesTitle = models.CharField(max_length=100, blank=False, null=False)
    Languages = models.CharField( blank=False, null=False)
    profile = models.ImageField(upload_to="profilePic/" ,blank=True, null=True)

    def __str__(self):
        return f"{self.selfIntroTitle} | {self.EducationTitle} | {self.LanguagesTitle}"
