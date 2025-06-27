from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models.skills import Skill
from .models.homeProject import HomeProject
from .models.Intro import Intro
from .models.Resume import Resume
from .serializers import SkillSerializer, HomeProjectSerializer, IntroSerializer, ResumeSerializer

@api_view(["GET"])
def get_skills(request):
    skills = Skill.objects.all() 
    serializer = SkillSerializer(skills, many=True)
    return Response(serializer.data)

# projects for home page
@api_view(["GET"])
def get_projects(request):  
    projects = HomeProject.objects.filter(show_on_homepage=True)
    serializer = HomeProjectSerializer(projects, many=True)
    return Response(serializer.data)

# projects for project page
@api_view(["GET"])
def get_projectPage(request):
    projects = HomeProject.objects.all()
    serializer = HomeProjectSerializer(projects, many=True)
    return Response(serializer.data)

# Abour me
@api_view(["GET"])
def get_intro(request):
    intro = Intro.objects.last()
    serializer = IntroSerializer(intro)
    return Response(serializer.data)

# resume

@api_view(["GET"])
def get_resume(request):
    file = Resume.objects.last()
    serializer = ResumeSerializer(file)
    return Response(serializer.data)

