from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase


# Create your tests here.
class UsersCrudBaseTest(APITestCase):
    def setUp(self) -> None:
        self.path = "/users/"

    def test_anon_user(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logged_user(self):
        my_admin = get_user_model().objects.create_superuser('myuser', 'myemail@test.com', "password")
        self.client.force_login(user=my_admin)
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
