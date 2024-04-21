from django.http import JsonResponse
from .models import Organisation
from .serializers import OrganisationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def organisation_list(request):

    if request.method == 'GET':
        organisation = Organisation.objects.all()
        serializer = OrganisationSerializer(organisation, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = OrganisationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def organisation_detail(request, id):

    try:
        organisation = Organisation.objects.get(pk=id)
    except Organisation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrganisationSerializer(organisation)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrganisationSerializer(organisation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        organisation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
