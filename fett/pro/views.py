from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import requirement
from .serializers import requirementSerializer
from rest_framework import serializers
from rest_framework import status
# Create your views here.

@api_view(['POST'])
def add_items(request):
    request.method == 'POST'
    serializer = requirementSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def view_items(request, pk):
    try:
        snippet = requirement.objects.get(pk=pk)
    except requirement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = requirementSerializer(snippet)
        return Response(serializer.data)


@api_view(['PUT'])
def update_items(request, pk):
    try:
        snippet = requirement.objects.get(pk=pk)
    except requirement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    request.method == 'PUT'
    serializer = requirementSerializer(snippet, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def delete_items(request, pk):
    try:
        snippet = requirement.objects.get(pk=pk)
    except requirement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    request.method == 'DELETE'
    snippet.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)