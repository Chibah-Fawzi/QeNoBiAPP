from django.shortcuts import render
from rest_framework import viewsets

from .models import Group
from .models import Link
from .serializers import GroupSerializer, LinkSerializer

# Create your views here.


class GroupView(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class LinkView(viewsets.ModelViewSet):

    queryset = Link.objects.all()
    serializer_class = LinkSerializer
