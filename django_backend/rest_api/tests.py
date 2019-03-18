from django.test import TestCase, Client
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import check_password
from django.urls import reverse

client = Client()
# Create your tests here.
class ApiTest(TestCase):
	""" Test module for API """

	def setUp(self):
		User.objects.create_user(username='user1',email='user1@email.com',password='password')

	def test_one_user(self):
		user1 = User.objects.get(username='user1')
		self.assertEqual(user1.username, 'user1')

	def test_user_password(self):
		user1 = User.objects.get(username='user1')
		self.assertEqual(check_password('password',user1.password), True)

	def test_get_all_users(self):
		response = client.get(reverse('get_all_users'))
		print(response.data)