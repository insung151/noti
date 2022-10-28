from rest_framework import serializers

from noti_manager.notification.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project

