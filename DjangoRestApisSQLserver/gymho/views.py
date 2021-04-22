# Create your views here.
# from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
# from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView

from gymho.models import Exercise, Customer
from gymho.serializers import ExerciseSerializer, LoginSerializer, CustomerSerializer

@api_view(['GET', 'POST', 'DELETE'])
class ExerciselistView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request):
        exercise = Exercise.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            exercise = Exercise.filter(title__icontains=title)

        exercise_serializer = ExerciseSerializer(exercise, many=True)
        return JsonResponse(exercise_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    @staticmethod
    def post(request):
        exercise_data = JSONParser().parse(request)
        exercise_serializer = ExerciseSerializer(data=exercise_data)
        if exercise_serializer.is_valid():
            exercise_serializer.save()
            return JsonResponse(exercise_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(exercise_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request):
        count = Exercise.objects.all().delete()
        return JsonResponse({'message': '{} Exercises were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def exercise_detail(request, pk):
    # find tutorial by pk (id)
    try:
        exercise = Exercise.objects.get(pk=pk)
    except Exercise.DoesNotExist:
        return JsonResponse({'message': 'The exercise does not exist'}, status=status.HTTP_404_NOT_FOUND)

        # GET / PUT / DELETE tutorial
    if request.method == 'GET':
        exercise_serializer = ExerciseSerializer(exercise)
        return JsonResponse(exercise_serializer.data)
    elif request.method == 'PUT':
        exercise_data = JSONParser().parse(request)
        exercise_serializer = ExerciseSerializer(exercise, data=exercise_data)
        if exercise_serializer.is_valid():
            exercise_serializer.save()
            return JsonResponse(exercise_serializer.data)
        return JsonResponse(exercise_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        exercise.delete()
        return JsonResponse({'message': 'exercise was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def exercise_list_published(request):
    # GET all published tutorials
    exercise = Exercise.objects.filter(published=True)

    if request.method == 'GET':
        exercise_serializer = ExerciseSerializer(exercise, many=True)
        return JsonResponse(exercise_serializer.data, safe=False)


class UserRegisterView(APIView):
    @staticmethod
    def post(request):
        # login = LoginSerializer(data=request.data)
        login_data = JSONParser().parse(request)
        login_serializer = LoginSerializer(data=login_data)
        if login_serializer.is_valid():
            login_serializer.validated_data['password'] = make_password(login_serializer.validated_data['password'])
            login_serializer.save()

            return JsonResponse(login_serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(login_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerView(APIView):
    permission_classes = (IsAdminUser,)

    @staticmethod
    def get(request):
        # GET list of tutorial, POST a new tutorial, DELETE all tutorial
        customer = Customer.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            customer = Customer.filter(title__icontains=title)

        customer_serializer = CustomerSerializer(customer, many=True)
        return JsonResponse(customer_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    @staticmethod
    def post(request):
        customer_data = JSONParser().parse(request)
        customer_serializer = CustomerSerializer(data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()

            return JsonResponse(customer_serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

