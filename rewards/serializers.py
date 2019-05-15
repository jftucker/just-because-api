from rest_framework import serializers
from .models import Reward


class RewardSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Reward