from rest_framework import serializers
from .models import Skill

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'level', 'category', 'icon', 'order', 'created_at']
        read_only_fields = ['id', 'created_at']