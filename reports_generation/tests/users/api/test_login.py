import pytest
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APIClient
from reports_generation.reports.models import User


@pytest.mark.django_db
def test_login_200(api_client: APIClient, user: User):
    response = api_client.post(
        '/api/v1/users/login/',
        data={
            'username': 'username',
            'password': 'password',
        },
    )

    assert response.status_code == HTTP_200_OK