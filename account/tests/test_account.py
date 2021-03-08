from django.test import TestCase
from django.contrib.auth import get_user_model
from account.models import Position, Team


# TODO: def create_user for each time creats

class UserTest(TestCase):
    """Test user"""
    def setUp(self):
        name_position = "Grphic"
        name_team = "BadAss"
        Position.objects.create(name=name_position)
        Team.objects.create(name=name_team)

    def test_create_user_none_team(self):
        name = 'jafar'
        last_name = 'babaii'
        email = 'hello@vye.com'
        username = 'abu'
        password = 'Hello-2342135'
        user = get_user_model().objects.create_user(
            name=name,
            last_name=last_name,
            email=email,
            username=username,
            password=password,
            team=None,
        )
        self.assertEquals(user.username, username.lower())
        self.assertEquals(user.email, email)

    # TODO: def test_create_user_with_team(self):
