
# Create your views here.

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from gymho.models import Execise
from gymho.serializers import ExeciseSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def execise_list(request):
    # GET list of tutorial, POST a new tutorial, DELETE all tutorial
    if request.method == 'GET':
        execise = Execise.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            execise = Execise.filter(title__icontains=title)

        execise_serializer = ExeciseSerializer(Execise, many=True)
        return JsonResponse(execise_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        execise_data = JSONParser().parse(request)
        execise_serializer = ExeciseSerializer(data=execise_data)
        if execise_serializer.is_valid():
            execise_serializer.save()
            return JsonResponse(execise_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(execise_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Execise.objects.all().delete()
        return JsonResponse({'message': '{} Execises were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def execise_detail(request, pk):
    # find tutorial by pk (id)
    try:
        execise = Execise.objects.get(pk=pk)
    except Execise.DoesNotExist:
        return JsonResponse({'message': 'The execise does not exist'}, status=status.HTTP_404_NOT_FOUND)

        # GET / PUT / DELETE tutorial
    if request.method == 'GET':
        execise_serializer = ExeciseSerializer(execise)
        return JsonResponse(execise_serializer.data)
    elif request.method == 'PUT':
        execise_data = JSONParser().parse(request)
        execise_serializer = ExeciseSerializer(execise, data=execise_data)
        if execise_serializer.is_valid():
            execise_serializer.save()
            return JsonResponse(execise_serializer.data)
        return JsonResponse(execise_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        execise.delete()
        return JsonResponse({'message': 'execise was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def execise_list_published(request):
    # GET all published tutorials
    execise = Execise.objects.filter(published=True)

    if request.method == 'GET':
        execise_serializer = ExeciseSerializer(execise, many=True)
        return JsonResponse(execise_serializer.data, safe=False)
