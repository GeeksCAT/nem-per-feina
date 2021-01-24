import pytest

from tests.factories import UserFactory


# Create your tests here.
@pytest.mark.django_db
class TestExample:
    def test__example__ok(self) -> None:
        user = UserFactory(first_name="Geeks", last_name=".CAT")
        assert user.first_name == "Geeks"


@pytest.mark.skip
@pytest.mark.django_db
def test_form_view(client, user_factory):
    from django.shortcuts import reverse

    breakpoint()
    user = user_factory()
    client.force_login(user=user)
    req = client.get(reverse("jobs:employer-jobs-create"))
