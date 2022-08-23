from typing import Any, Dict
import pytest


@pytest.fixture()
def user_registration_data() -> Dict[str, Any]:
    return {
        'username': 'username',
        'email': 'username@gmail.com',
        'password1': 'password',
        'password2': 'password',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'patronymic': 'patronymic',
        'extra_information': '',
    }
