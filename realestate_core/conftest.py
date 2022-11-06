import pytest
from django.contrib.auth.models import User

from realestate_core.models import Realtor, Realestate


@pytest.fixture
def user():
    return User.objects.create_superuser(username='jakub', password='jakub', is_active=True)

@pytest.fixture
def realtor(user):
    return Realtor.objects.create(user=user, bio="xxx")

@pytest.fixture
def realestate():
    return Realestate.objects.create(price=300000)