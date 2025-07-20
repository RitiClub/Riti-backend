from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

# View for Riti model
class RitiListView(APIView):
    def get(self, request):
        riti = Riti.objects.all()
        serializer = RitiSerializer(riti, many=True)
        return Response(serializer.data)

# View for Members model
class MembersListView(APIView):
    def get(self, request):
        members = Members.objects.all()
        serializer = MembersSerializer(members, many=True)
        return Response(serializer.data)

# View for Carsol model
class CarsolListView(APIView):
    def get(self, request):
        carsol = Carsol.objects.all()
        serializer = CarsolSerializer(carsol, many=True)
        return Response(serializer.data)

# View for Logo model
class LogoListView(APIView):
    def get(self, request):
        logos = Logo.objects.all()
        serializer = LogoSerializer(logos, many=True)
        return Response(serializer.data)

# View for Recruitment model
class RecruitmentListView(APIView):
    def get(self, request):
        recruitment = Recruitment.objects.all()
        serializer = RecruitmentSerializer(recruitment, many=True)
        return Response(serializer.data)

# View for Team model
class TeamListView(APIView):
    def get(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

# View for TeamImages model
class TeamImagesListView(APIView):
    def get(self, request):
        team_images = TeamImages.objects.all()
        serializer = TeamImagesSerializer(team_images, many=True)
        return Response(serializer.data)

# View for Magzine model
class MagzineListView(APIView):
    def get(self, request):
        magzine = Magzine.objects.all()
        serializer = MagzineSerializer(magzine, many=True)
        return Response(serializer.data)

# View for MagImages model
class MagImagesListView(APIView):
    def get(self, request):
        mag_images = MagImages.objects.all()
        serializer = MagImagesSerializer(mag_images, many=True)
        return Response(serializer.data)
