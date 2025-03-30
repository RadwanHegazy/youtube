from django.test import TestCase
from django.urls import reverse
from globals.test_objects import create_user, create_video, create_headers


class TestHistoryEndpoint (TestCase) : 

    def setUp(self):
        self.history_endpoint = reverse('user_history')
        self.user = create_user()
        self.headers = create_headers(self.user)

    def test_unauthorized(self):
        req = self.client.get(self.history_endpoint)
        self.assertEqual(req.status_code, 401)
    
    def test_empty_response(self) : 
        req = self.client.get(self.history_endpoint, headers=self.headers)
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['count'], 0)
    
    def test_non_empty_response(self) : 
        self.user.history.add(create_video())
        self.user.save()
        req = self.client.get(self.history_endpoint, headers=self.headers)
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['count'], 1)
    

