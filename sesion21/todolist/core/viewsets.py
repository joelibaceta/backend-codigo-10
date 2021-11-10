
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework import status

from core.serializers import TaskSerializer, UserLoginSerializer

from core.models import Task

class UserViewset(viewsets.ViewSet):

    def login(self, request):

        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid():
            user, token = serializer.save()
            data = {
                'username': f"{user.first_name}  {user.last_name}",
                'access_token': token
            }
            return Response(data)
        else:
            return Response(serializer.errors)

class TaskViewSet(viewsets.ViewSet):

    def list(self, request):
        user = request.user
        if user.is_anonymous:
            return Response({"error": "not found"}, status.HTTP_404_NOT_FOUND)
        else:
            tasks = Task.objects.filter(user_id=user.id)
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data)
    
    def create(self, request):
        data = request.data
        print(request.user)
        if not request.user.is_anonymous:
            data["user_id"] = request.user.id
        else:
            return Response({"error": "Invalid Token!"}, status.HTTP_401_UNAUTHORIZED)
        
        serializer = TaskSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def update(self, request, pk):
        if not request.user.is_anonymous:
            tasks = Task.objects.filter(pk = pk)
            if request.user.id == tasks.first().user_id:
                data = request.data
                if not "user_id" in data:
                    tasks.update(**data)
                    return Response({"status": "OK"}, status.HTTP_201_CREATED)
                else:
                    return Response({"status": "para, user_id is not allowed"}, status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error": "You can update only your own tasks!"}, status.HTTP_403_FORBIDDEN)
        else:
            return Response({"error": "Invalid Token!"}, status.HTTP_401_UNAUTHORIZED)
        
    def destroy(self, request, pk):
        if not request.user.is_anonymous:
            tasks = Task.objects.filter(pk = pk)
            if request.user.id == tasks.first().user_id:
                tasks.delete()
                return Response({"status": "OK"})
            else:
                return Response({"error": "You can delete only your own tasks!"}, status.HTTP_403_FORBIDDEN)
        else:
            return Response({"error": "Invalid Token!"}, status.HTTP_401_UNAUTHORIZED)
