from .models import Profile,Experience
from rest_framework import serializers

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ('title', 'company', 'logo', 'date', 'description')

# Serializers define the API representation.
class ProfileSerializer(serializers.ModelSerializer):
    experiences = ExperienceSerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = ['name', 'short_description', 'description', 'image', 'updated','experiences']
