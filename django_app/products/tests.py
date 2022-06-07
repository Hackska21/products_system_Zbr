from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase


# Create your tests here.
# Create your tests here.
class ProductsCrudBaseTest(APITestCase):
    def setUp(self) -> None:
        self.path = "/products/"

    def create_product(self):
        response = self.client.post(
            self.path,
            {
                "price": "41.35",
                "sku": "dasda",
                "brand": "dfsdf"
            },
            "json"
        )
        return response

    def log_admin(self):
        my_admin = get_user_model().objects.create_superuser('myuser', 'myemail@test.com', "password")
        self.client.force_login(user=my_admin)

    def test_anon_user(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_user(self):
        self.log_admin()
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_creation_anon(self):
        response = self.create_product()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_creation_admin(self):
        self.log_admin()
        response = self.create_product()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_admin(self):
        self.log_admin()
        response = self.create_product()
        product_id = response.json()['id']
        product_path = f"{self.path}{product_id}/"
        retrieve_response = self.client.get(product_path)
        self.assertEqual(retrieve_response.status_code, status.HTTP_200_OK)
        count = retrieve_response.json()['retrieve_count']
        self.assertEqual(count, 0)

    def test_retrieve_anon(self):
        self.log_admin()
        response = self.create_product()
        product_id = response.json()['id']

        # logout
        self.client.logout()
        product_path = f"{self.path}{product_id}/"
        retrieve_response = self.client.get(product_path)
        self.assertEqual(retrieve_response.status_code, status.HTTP_200_OK)
        count = retrieve_response.json()['retrieve_count']
        self.assertEqual(count, 1)

