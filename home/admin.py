from django.contrib import admin
from .models.skills import Skill
from .models.homeProject import HomeProject
from .models.Intro import Intro
from .models.Resume import Resume


# Register your models here.

class HomeProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'githubLink', 'show_on_homepage')
    list_editable = ('show_on_homepage',)
    filter_horizontal = ('skills',)

admin.site.register(Skill)
admin.site.register(Intro)
admin.site.register(Resume)
admin.site.register(HomeProject, HomeProjectAdmin)



