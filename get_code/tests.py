from django.test import TestCase
from get_code.views import index
# Create your tests here.


class TestResponse(TestCase):
    def test_a_response_200(self):
        response = self.client.get("/secret/")
        self.assertEqual(response.status_code, 200)


    def test_b_response_is_json(self):
        import json
        state = True
        response = self.client.get("/secret/")
        try:
            response = json.loads(response.content)
        except json.decoder.JSONDecodeError:
            state = False
        self.assertTrue(state, "Could not convert item to dictionary")
        

        
