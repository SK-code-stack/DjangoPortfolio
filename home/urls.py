from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path("skill/", views.get_skills, name="skill"),
    path("HomeProject/", views.get_projects, name="HomeProject"),
    path("intro/", views.get_intro, name="intro"),
    path("resume/", views.get_resume, name="resume"),
    path("projectPage/", views.get_projectPage, name="projectPage"),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)