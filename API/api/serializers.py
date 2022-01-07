from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
from API import models
from API import *
import secrets
import string

class UserSerializers(serializers.ModelSerializer):


	def validate(self, data):

		if data["password"] == '':
		
			alphabet = string.ascii_letters + string.digits
			password = ''.join(secrets.choice(alphabet) for i in range(4,21))
			data['password']=password
		
		data['password']=make_password(data['password'])
		return data

	class Meta:
		model  = models.User
		fields = '__all__'

	
