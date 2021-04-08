
# Create your views here.

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from gymho.models import Exercise
from gymho.serializers import ExerciseSerializer
from rest_framework.decorators import api_view


def exercise_serializer(args):
    pass


@api_view(['GET', 'POST', 'DELETE'])
def exercise_list(request):
    # GET list of tutorial, POST a new tutorial, DELETE all tutorial
    if request.method == 'GET':
        exercise = Exercise.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            exercise = Exercise.filter(title__icontains=title)

        exercise_serializer = ExerciseSerializer(Exercise, many=True)
        return JsonResponse(exercise_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        exercise_data = JSONParser().parse(request)
        exercise_serializer = ExerciseSerializer(data=exercise_data)
        if exercise_serializer.is_valid():
            exercise_serializer.save()
            return JsonResponse(exercise_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(exercise_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
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
