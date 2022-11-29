from django.shortcuts import render
from rest_framework.response import Response
from .models import forum
from rest_framework.decorators import api_view
from .serializers import forumSerializer
from rest_framework import status
# Create your views here.
@api_view(['POST'])
def forumview(request):
    serializer=forumSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):  
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def getview(request):
    request.method == 'GET'
    snippets = forum.objects.all()
    serializer = forumSerializer(snippets, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
def getputview(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = forum.objects.get(pk=pk)
    except forum.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = forumSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = forumSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)