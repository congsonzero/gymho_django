from rest_framework import serializers
from gymho.models import Execise


class ExeciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Execise
        fields = ('ExeciseID',
                  'name',
                  'rep_recommend',
                  'Active')
