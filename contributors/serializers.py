from rest_framework import serializers
from .models import Contributor


class ContributorSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Contributor