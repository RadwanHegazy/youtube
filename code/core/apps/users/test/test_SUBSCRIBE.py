from django.test import TestCase
from globals.test_objects import create_user, create_headers
from django.urls import reverse

class TestSubscribeEndpoint(TestCase) : 

    def setUp(self):
        self.subscribe_endpoint = reverse('subscribe_user')
        self.user = create_user()
        self.headers = create_headers(self.user)
        

    def test_subscribe_unauthorized(self) : 
        req = self.client.post(self.subscribe_endpoint)
        self.assertEqual(req.status_code, 401)

    def test_subscribe_no_body(self) : 
        req = self.client.post(self.subscribe_endpoint, headers=self.headers)
        self.assertEqual(req.status_code, 400)
    
    def test_subscribe_same_user(self) : 
        data = {
            'user_id' : self.user.id
        }
        req = self.client.post(self.subscribe_endpoint, headers=self.headers, data=data)
        self.assertEqual(req.status_code, 400)
    
    def test_subscribe_user_not_found(self) : 
        data = {
            'user_id' : 999
        }
        req = self.client.post(self.subscribe_endpoint, headers=self.headers, data=data)
        self.assertEqual(req.status_code, 400)
    
    def test_subscribe_success(self) :
        new_user = create_user() 
        data = {
            'user_id' : new_user.id
        }
        req = self.client.post(self.subscribe_endpoint, headers=self.headers, data=data)
        self.assertEqual(req.status_code, 201)
        self.assertIn(self.user, new_user.subscriptions.all())
        self.assertIn(new_user, self.user.subscribe_to.all())