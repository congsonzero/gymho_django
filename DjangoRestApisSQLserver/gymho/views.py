# Create your views here.
# from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.http.response import JsonResponse, Http404
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
# from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView

from gymho.models import Exercise, Customer, Login, Todo
from gymho.serializers import ExerciseSerializer, LoginSerializer, CustomerSerializer, TodoSerializer


# from gymho.permission import Userpermissions


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


class UserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Login.objects.get(pk=pk)
        except Login.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        if request.user.Login_id != int(pk):
            return JsonResponse({'message': 'error'}, status=status.HTTP_400_BAD_REQUEST)
        login = self.get_object(pk)
        serializer = LoginSerializer(login)
        return JsonResponse(serializer.data)


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


class UserLoginView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Customer.objects.get(Login_id=pk)
        except Customer.DoesNotExist:
            raise Http404

    def CustomerID(self, request, pk):
        if request.user.Login_id != int(pk):
            return JsonResponse({'message': 'error'}, status=status.HTTP_400_BAD_REQUEST)
        customer = self.get_object(pk)
        return customer.User_id

    def get(self,request,pk):
        userid=self.CustomerID(request,pk)
        # customer = self.get_object(pk)
        customer = Customer.objects.all().filter(age=18)
        # print(customer[0])
        #
        # serializer = CustomerSerializer(customer[0])
        # print(serializer)
        todo = Todo.objects.raw('select * from Todo where UserID=8 go')
        print(todo)
        serializer = TodoSerializer(todo)
        return JsonResponse(serializer.data, safe=False)