from .models import Profile,Experience, Skill, Education, Social 
from rest_framework import serializers
from django.views.decorators.http import require_http_methods


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('name', 'icon')

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('name', 'short_description', 'icon', 'link', 'type_education')


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ('title', 'company', 'logo', 'date', 'description', 'type_experience', 'skills')


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ('name', 'link', 'icon')  

 


class ProfileSerializer(serializers.ModelSerializer):
    experiences = ExperienceSerializer(many=True, read_only=True)
    educations = EducationSerializer(many=True, read_only=True)
    socials = SocialSerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = ['name', 'short_description', 'description', 'image', 'updated','experiences', 'educations', 'socials']


