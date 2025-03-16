from django.test import TestCase
from django.urls import reverse
from globals.test_objects import create_user, create_headers

class TestProfileEndpoint (TestCase) :

    def setUp(self):
        self.profile_url = reverse('profile')
        self.user = create_user()

    def test_get_unauthenticated(self) : 
        req = self.client.get(self.profile_url)
        self.assertEqual(req.status_code, 401)
    
    def test_get_success(self) : 
        req = self.client.get(self.profile_url, headers=create_headers(self.user))
        res = req.json()
        self.assertEqual(req.status_code, 200)
        self.assertEqual(res['id'], self.user.id)
        self.assertEqual(res['email'], self.user.email)
        self.assertEqual(res['username'], self.user.username)

        