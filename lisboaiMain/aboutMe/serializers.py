from .models import Profile,Experience
from rest_framework import serializers

# Serializers define the API representation.
class ProfileSerializer(serializers.ModelSerializer):
    experiences = serializers.StringRelatedField(many=True)
    class Meta:
        model = Profile
        fields = ['name', 'short_description', 'description', 'image', 'updated','experiences']
