from typing import Any, Dict
import pytest
from django.forms import model_to_dict
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.test import APIClient
from reports_generation.reports.models import User


@pytest.mark.django_db
def test_registration_200_project(
    api_client: APIClient,
    user_registration_data: Dict[str, Any],

):
    response = api_client.post('/api/v1/users/registration/', data=user_registration_data)

    user = User.objects.get()
    assert response.status_code == HTTP_201_CREATED
    assert model_to_dict(
        user,
        exclude=(
            'password1',
            'password2',
            'date_joined',
            'is_staff',
            'password',
            'last_login',
            'user_permissions',
            'groups',
        ),
    ) == {
        'id': user.id,
        'username': user_registration_data['username'],
        'email': user_registration_data['email'],
        'first_name': user_registration_data['first_name'],
        'last_name': user_registration_data['last_name'],
        'patronymic': user_registration_data['patronymic'],
        'is_active': True,
        'is_superuser': False,
        'extra_information': '',
    }
    assert response.json() == {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'patronymic': user.patronymic,
        'extra_information': '',
    }




@pytest.mark.django_db
def test_registration_400_password_differ(
    api_client: APIClient,
    user_registration_data: Dict[str, Any],
):
    user_registration_data['password1'] = 'password1'
    user_registration_data['password2'] = 'password2'

    response = api_client.post('/api/v1/users/registration/', data=user_registration_data)

    assert response.status_code == HTTP_400_BAD_REQUEST
    assert response.json() == {'non_field_errors': ["Passwords don't match; Пароли не совпадают"]}




