from .models import Profile,Experience, Skill, Education, Social
from rest_framework import serializers



class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('name', 'icon')


class ExperienceSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    class Meta:
        model = Experience
        fields = ('title', 'company', 'logo', 'date', 'description', 'skills')


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('short_description', 'icon', 'link', 'type_education', 'position')


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ('name', 'icon', 'link')        

# Serializers define the API representation.
class ProfileSerializer(serializers.ModelSerializer):
    experiences = ExperienceSerializer(many=True, read_only=True)
    educations = EducationSerializer(many=True, read_only=True)
    socials = EducationSerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = ['name', 'short_description', 'description', 'image', 'updated','experiences', 'educations', 'socials']


