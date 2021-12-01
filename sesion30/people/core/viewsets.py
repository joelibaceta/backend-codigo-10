from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from core.models import Person

class PeopleViewSet(ViewSet):

    def create(self, request):
        data = request.data
        print(data)
        person = Person.insert(data)
        return Response(data, status=status.HTTP_201_CREATED)
