from rest_framework import serializers
from .models import MemberModel


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberModel
        fields = ['name','email']