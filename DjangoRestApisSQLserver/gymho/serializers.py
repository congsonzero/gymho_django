from rest_framework import serializers
from gymho.models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('ExerciseID',
                  'name',
                  'rep_recommend',
                  'Activate')