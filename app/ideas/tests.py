import pytest
from django.test import RequestFactory, TestCase
from graphene.test import Client
from mixer.backend.django import mixer

from users.models import CustomUser
from ideas.schema import schema


create_idea_mutation = """
    mutation {
        createIdea(input: {content:"asd", visibility:"public"}) {
            idea {
            id,
            content,
            dateCreated,
            visibility
            }
        }
    }
"""

my_ideas_query = """
    query {
        myIdeas {
            id,
            content,
            dateCreated,
            visibility
        }
    }
"""

@pytest.mark.django_db
class AnExampleTest(TestCase):

    def setUp(self):
        self.client = Client(schema)
        self.my_request = RequestFactory().get("")
        self.my_request.user = mixer.blend(CustomUser)

    def test_create_idea(self):
        response = self.client.execute(create_idea_mutation, context_value=self.my_request)
        res = response.get('data').get('createIdea').get('idea')
        
        self.assertEqual(res.get('content'), 'asd')
        self.assertEqual(res.get('visibility'), 'PUBLIC')

    def test_my_ideas(self):
        created_idea = self.client.execute(create_idea_mutation, context_value=self.my_request)
        created_idea = created_idea.get('data').get('createIdea').get('idea')
        response = self.client.execute(my_ideas_query, context_value=self.my_request)
        res = response.get('data').get('myIdeas')
        
        self.assertIn(created_idea, res)

