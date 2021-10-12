import pytest
from django.test import RequestFactory, TestCase
from graphene.test import Client
from mixer.backend.django import mixer

from users.models import CustomUser
from users.schema import schema


register_mutation = """
    mutation {
        register(email:"fake@fake.com", username: "fakeUser", password1:"EUPp9xe*mX$7", password2:"EUPp9xe*mX$7") {
            success,
            errors,
            token,
            refreshToken
        }
    }
"""

login_mutation = """
    mutation {
        login(username: "fakeUser", password:"EUPp9xe*mX$7") {
            success,
            errors,
            token,
            refreshToken,
            user {
                id, email, username
            }
        }
    }
"""

users_query = """
    query {
        users {
            id,
            username,
            email
        }
    }
"""

@pytest.mark.django_db
class AnExampleTest(TestCase):

    def setUp(self):
        self.client = Client(schema)
        self.my_request = RequestFactory().get("")
        self.my_request.user = mixer.blend(CustomUser)

    def test_register(self):
        response = self.client.execute(register_mutation, context_value=self.my_request)
        res = response.get('data').get('register')

        self.assertEqual(res.get('success'), True)
        self.assertIsNone(res.get('errors'))
        self.assertIsNotNone(res.get('token'))

    def test_login(self):
        self.client.execute(register_mutation, context_value=self.my_request)
        response = self.client.execute(login_mutation, context_value=self.my_request)
        res = response.get('data').get('login')
        self.token = res.get('token')

        self.assertEqual(res.get('success'), True)
        self.assertIsNone(res.get('errors'))
        self.assertIsNotNone(res.get('token'))
        self.assertEqual(res.get('user').get('email'), 'fake@fake.com')
        self.assertEqual(res.get('user').get('username'), 'fakeUser')

    def test_users(self):
        mixer.blend(CustomUser)
        mixer.blend(CustomUser)
        response = self.client.execute(users_query, context_value=self.my_request)
        res = response.get('data').get('users')
        
        assert len(res) >= 0
    