from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Skill
from .serializers import SkillSerializer

class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [AllowAny]
