from rest_framework import serializers
from API import models
from API import *
import secrets
import string

class UserSerializers(serializers.ModelSerializer):


	def to_representation(self, data):
			
		data = super(UserSerializers, self).to_representation(data)
		
		if data.get('password') == "":
		
			alphabet = string.ascii_letters + string.digits
			password = ''.join(secrets.choice(alphabet) for i in range(4,21))
			
			data['password']=password
	
		return data

	class Meta:
		model  = models.User
		fields = '__all__'

	
