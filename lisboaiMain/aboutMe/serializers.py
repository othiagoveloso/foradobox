from .models import Profile,Experience
from rest_framework import serializers

# Serializers define the API representation.
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'short_description', 'description', 'image', 'updated')


class ExperienceSerializer(serializers.ModelSerializer):
    user = ProfileSerializer()
    class Meta:
        model = Experience
        fields = ('user', 'title', 'company', 'logo', 'date','description')        

        def create(self, validated_data):
            user_data = validated_data.pop('user')  
            user_ser = User.objects.create(**user_data)
            experience = Experience.objects.create(user=user_ser, **user_data)
            return experience