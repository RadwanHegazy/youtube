from django.test import TestCase
from django.urls import reverse
from apps.social_auth.platforms import GoogleAuth


class TestGoogleAuth (TestCase) :

    def setUp(self):
        self.get_google_url = reverse('google_url')
        self.google_auth_url = reverse('google_auth')

    def test_get_success_url(self) : 
        req = self.client.get(self.get_google_url)
        url = GoogleAuth().get_auth_url()
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['url'], url)

    def test_get_code(self) :
        req = self.client.get(self.google_auth_url)
        self.assertNotEqual(req.status_code, 200)
    
    def test_post_code_empty(self) : 
        req = self.client.post(self.google_auth_url, data={})
        self.assertEqual(req.status_code, 400)
        
    def test_post_invaild_code(self) : 
        req = self.client.post(self.google_auth_url, data={
            'code' : 'asdasd123123'
        })
        self.assertEqual(req.status_code, 400)
