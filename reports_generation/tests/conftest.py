import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from reports_generation.tests.factory.users import UserFactory


@pytest.fixture()
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture()
def user() -> User:
    return UserFactory(username='username', password='password')


@pytest.fixture()
def authorized_api_client(api_client: APIClient, user: User) -> APIClient:
    api_client.force_authenticate(user)
    return api_client
