from django.test import TestCase
from globals.test_objects import create_user, create_headers
from django.urls import reverse

class TestUnSubscribeEndpoint(TestCase) : 

    def setUp(self):
        self.unsubscribe_endpoint = reverse('unsubscribe_user')
        self.user = create_user()
        self.headers = create_headers(self.user)
        

    def test_unsubscribe_unauthorized(self) : 
        req = self.client.post(self.unsubscribe_endpoint)
        self.assertEqual(req.status_code, 401)

    def test_unsubscribe_no_body(self) : 
        req = self.client.post(self.unsubscribe_endpoint, headers=self.headers)
        self.assertEqual(req.status_code, 400)
    
    def test_unsubscribe_same_user(self) : 
        data = {
            'user_id' : self.user.id
        }
        req = self.client.post(self.unsubscribe_endpoint, headers=self.headers, data=data)
        self.assertEqual(req.status_code, 400)
    
    def test_unsubscribe_user_not_found(self) : 
        data = {
            'user_id' : 999
        }
        req = self.client.post(self.unsubscribe_endpoint, headers=self.headers, data=data)
        self.assertEqual(req.status_code, 400)
    
    def test_unsubscribe_success(self) :
        new_user = create_user()
        new_user.subscriptions.add(self.user)
        self.user.subscribe_to.add(self.user)
        new_user.save()
        self.user.save()
        data = {
            'user_id' : new_user.id
        }
        req = self.client.post(self.unsubscribe_endpoint, headers=self.headers, data=data)
        self.assertEqual(req.status_code, 201)
        self.assertNotIn(self.user, new_user.subscriptions.all())
        self.assertNotIn(new_user, self.user.subscribe_to.all())
    
    