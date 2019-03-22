from django.contrib.auth.models import User, Group
from rest_framework import serializers, status
from rest_framework.response import Response


class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	group = serializers.CharField(write_only=True)

	def validate_group(self, value):
		try:
			group_names = Group.objects.get(name=value)
		except Group.DoesNotExist:
			raise serializers.ValidationError("Invalid group name")
		return value

	def create(self, validated_data):
		user = User.objects.create(
			username=validated_data['username'],
			email=validated_data['email'],
			first_name=validated_data['first_name'],
			last_name=validated_data['last_name']
		)
		user.set_password(validated_data['password'])
		group = Group.objects.get(name=validated_data['group'])
		user.groups.add(group)

		user.save()

		return user

	class Meta:
		model = User
		fields = ('username', 'email', 'groups', 'first_name', 'last_name', 'password','group')
		extra_kwargs = {'email': {'required': True}, 'first_name': {'required': True}, 'last_name': {'required': True}, 'group': {'required': True}} 


class GroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group
		fields = ('name')