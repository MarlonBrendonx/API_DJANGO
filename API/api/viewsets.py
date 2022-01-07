from rest_framework import viewsets
from API.api import serializers
from API import models

class UserViewSet(viewsets.ModelViewSet):

	serializer_class = serializers.UserSerializers	
	queryset = models.User.objects.all()

