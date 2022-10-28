from rest_framework import serializers

from notification.models import *


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class SignInSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()


class SignUpSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
    username = serializers.CharField()

class TargetSerializer(serializers.Serializer):

    class Meta:
        model = TargetUser
        fields= '__all__'


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageTemplate
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


class NotificationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationLog
        fields = '__all__'
