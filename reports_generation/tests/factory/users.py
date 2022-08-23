from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyText
from faker import Faker
from reports_generation.reports.models import User

fake = Faker()


class UserFactory(DjangoModelFactory):
    email = fake.email()
    username = FuzzyText()
    password = FuzzyText()
    first_name = FuzzyText()
    last_name = FuzzyText()
    patronymic = FuzzyText()
    is_active = True
    is_staff = False
    extra_information = FuzzyText()

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        user = cls._get_manager(model_class)
        if 'is_superuser' in kwargs:
            return user.create_superuser(*args, **kwargs)
        else:
            return user.create_user(*args, **kwargs)

    class Meta:
        model = User
