from rest_framework import serializers
from api.models import Predict_log


class PredictLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Predict_log
        fields = '__all__'