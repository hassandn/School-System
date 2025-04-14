from django.test import TestCase
from .models import CustomUser
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class JwtAuthenticationTest(APITestCase):
    @classmethod
    def setUpTestData(cls):#create user
        cls.user = CustomUser.objects.create_user(
            username="testuser",
            password="testpassword",
            national_id="01234",
            email="tsetuser@gmail.com",
            bio="this is a test bio",
            registration_status=True,
            role="Admin",
        )

    def setUp(self):#get access token and refresh token 
        token_url = reverse("token_obtain_pair")
        response = self.client.post(
            token_url, {"username": "testuser", "password": "testpassword"}
        )
        self.token_response = response
        self.refresh_token = response.data["refresh"]
        self.access_token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

    def test_obtain_jwt_token_status_code(self):# url for get tokens status code
        response = self.client.post(
            token_url, {"username": "testuser", "password": "testpassword"}
        )
        token_url = reverse("token_obtain_pair")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_obtain_jwt_token_status_code(self):#url for get tokens contains access token
        self.assertEqual(self.token_response.status_code, status.HTTP_200_OK)

    def test_obtain_jwt_access_token(self):# url for get tokens contains access token
        self.assertIn("access", self.token_response.data)

    def test_obtain_jwt_refresh_token(self):# url for get tokens contains refresh token
        self.assertIn("refresh", self.token_response.data)

    def test_logout_status_code(self):# tests logout status code
        logout_url = reverse("logout")
        response = self.client.post(logout_url, {"refresh_token": self.refresh_token})
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)

    def test_logout_if_has_response_message(self):# checks if logout has message
        logout_url = reverse("logout")
        response = self.client.post(logout_url, {"refresh_token": self.refresh_token})
        self.assertIn("detail", response.data)

    def test_logout_response_message(self):# checks lougout message
        logout_url = reverse("logout")
        response = self.client.post(logout_url, {"refresh_token": self.refresh_token})
        ideal_response_message = {'detail': 'Successfully logged out.'}
        self.assertEqual(response.data, ideal_response_message)
