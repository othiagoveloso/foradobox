from .models import Profile,Experience
from rest_framework import serializers

# Serializers define the API representation.
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'short_description', 'description', 'image', 'updated')

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ('user', 'title', 'company', 'logo', 'date','description')        