from django.test import TestCase
from django.contrib.auth import get_user_model
from account.models import Position, Team


def sample_user(firs_name='jafar',
                last_name='babaii',
                email='hello@vye.com',
                username='abu',
                password='Hello-2342135',
                team=None,
                position=None
                ):

    """Creates a sample User without team object"""
    user = get_user_model().objects.create_user(
        first_name=firs_name,
        last_name=last_name,
        email=email,
        username=username,
        password=password,
        team=team,
        position=position
    )
    return user


class AccountTest(TestCase):
    """Test Account model"""

    def test_create_user_none_team_and_position(self):
        """Creates User without team name"""
        username = 'opsopsbombom'
        email = 'opsopsbombom@gmail.com'
        password = 'bahbah-2342135'

        user = sample_user(email=email, username=username, password=password)
        self.assertEquals(user.username, username.lower())
        self.assertEquals(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_with_team(self):
        """Crates User with team name"""
        team_name = Team.objects.create(name='Abbbasia')
        user = sample_user(team=team_name)
        self.assertEquals(user.team, team_name)

    def test_create_user_witth_team_and_poition(self):
        """Create User with team and postion"""
        name_position = "Grphic"
        position = Position.objects.create(name=name_position)
        team_name = Team.objects.create(name='Abbbasia')
        user = sample_user(team=team_name, position=position)
        self.assertEquals(user.team, team_name)
