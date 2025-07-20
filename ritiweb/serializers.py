from rest_framework import serializers
from .models import Riti, Members, Carsol, Logo, Recruitment, Team, TeamImages, Magzine, MagImages

# Serializer for Riti model
class RitiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Riti
        fields = ['batch']

# Serializer for Members model
class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ['batch', 'name', 'role']

# Serializer for Carsol model
class CarsolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carsol
        fields = ['image', 'caption']

# Serializer for Logo model
class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = ['image']

# Serializer for Recruitment model
class RecruitmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruitment
        fields = ['stage', 'name', 'description', 'link']

# Serializer for Team model
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['batch', 'link', 'description']

# Serializer for TeamImages model
class TeamImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamImages
        fields = ['batch', 'image']

# Serializer for Magzine model
class MagzineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magzine
        fields = ['mag_id']

# Serializer for MagImages model
class MagImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MagImages
        fields = ['mag_id', 'image']
