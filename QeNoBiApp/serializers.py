from rest_framework import serializers
from .models import Group, Link


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'user', 'item', 'period', 'depth', 'support')


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('id', 'user', 'group_target', 'group_source')
