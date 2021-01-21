import factory
import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from django.conf import settings

from geolocation.geo_utils import GeoCoder
from tests.factories import AddressFactory, JobFactory, UserFactory

# Register factories to pytest global namespace.
# They can be access as normal fixtures using user_factory or job_factory.
register(UserFactory)
register(JobFactory)
register(AddressFactory)


def pytest_configure():
    """
    Use for override default settings
    https://pytest-django.readthedocs.io/en/latest/configuring_django.html#using-django-conf-settings-configure
    """
    settings.CELERY_TASK_ALWAYS_EAGER = True
    settings.EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def api_client_authenticate(db, user_factory, api_client):
    def _api_client(user=None):
        """Allows pass custom user object."""
        if user is None:
            user = user_factory()
        api_client.force_authenticate(user=user)
        return api_client

    yield _api_client
    api_client.force_authenticate(user=None)


@pytest.fixture
def create_job(db, job_factory):
    return job_factory


@pytest.fixture
def create_job_as_dict(db, job_factory) -> dict:
    return factory.build(dict, FACTORY_CLASS=JobFactory)


@pytest.fixture
def create_jobs(db, job_factory):
    def _create_jobs(size=10):
        return job_factory.simple_generate_batch(create=True, size=size)

    return _create_jobs


@pytest.fixture
def create_users(db, user_factory):
    def _create_users(size=5):
        return user_factory.simple_generate_batch(create=True, size=size)

    return _create_users


import random


@pytest.fixture
def complete_address_records(address_factory, job_factory):
    address_list = [address_factory(city="Girona"), address_factory(city="Barcelona")]
    location = GeoCoder()
    for _ in range(5):
        address = random.choice(address_list)
        location.get_coordinates(address=address.full_address)
        address.set_coordinates(location.lat, location.lon)
        job_factory(geo_location=address)

    return address_list
