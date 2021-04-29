from rest_framework import serializers
from gymho import models
from gymho.models import Exercise, Customer, Login, Todo


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('ExerciseID',
                  'name',
                  'rep_recommend',
                  'Activate')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('User_id',
                  'name',
                  'address',
                  'age',
                  'weight',
                  'height',
                  # 'ExerciseProgram',
                  'Login',
                  )


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ('username', 'password', 'email', 'is_staff')
        extra_kwargs = {'password': {'write_only': True}}

        @staticmethod
        def create(self, validated_data):
            user = models.Login(
                email=validated_data['email'],
                username=validated_data['username']
            )
            user.set_password(validated_data['password'])
            user.save()

            return user


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('TodoID', 'User',)
