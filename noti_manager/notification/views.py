from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from notification.serializers import ProjectSerializer, TargetSerializer, SignUpSerializer, \
    SignInSerializer, TemplateSerializer, NotificationSerializer, NotificationLogSerializer


class SignUpView(GenericAPIView, CreateModelMixin):
    serializer_class = SignUpSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SignInView(CreateModelMixin, GenericAPIView):
    serializer_class = SignInSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer


class TargetsViewSet(
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    GenericViewSet
):
    serializer_class = TargetSerializer

class TemplateViewSet(ListModelMixin, GenericViewSet):
    serializer_class = TemplateSerializer

class Notification(ModelViewSet):
    serializer_class = NotificationSerializer


class NotificationLog(ListModelMixin, GenericViewSet):
    serializer_class = NotificationLogSerializer