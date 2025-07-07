from rest_framework import serializers
from .models.skills import Skill
from .models.homeProject import HomeProject
from .models.Intro import Intro
from .models.Resume import Resume

class SkillSerializer(serializers.ModelSerializer):  # For full skill info (with icon)
    class Meta:
        model = Skill
        fields = '__all__'

class MiniSkillSerializer(serializers.ModelSerializer):  # For use in projects only
    class Meta:
        model = Skill
        fields = ['name']
# project serializer
class HomeProjectSerializer(serializers.ModelSerializer):  # Corrected spelling here too
    skills = MiniSkillSerializer(many=True, read_only=True)

    class Meta:
        model = HomeProject
        fields = ['id', 'title', 'description', 'image', 'skills', 'githubLink']

# about me
class IntroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intro
        fields = '__all__'

# resume 
class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'