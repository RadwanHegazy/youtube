from rest_framework.test import APITestCase
from django.urls import reverse
from globals.test_objects import create_user, create_headers

class TestCreatePlaylistEndpoint (APITestCase) : 

    def setUp(self):
        self.create_playlist_endpoint = reverse('create_playlist')
        self.user = create_user()
        self.headers = create_headers(self.user)

    def test_create_unauhorized(self) : 
        req = self.client.post(self.create_playlist_endpoint)
        self.assertEqual(req.status_code, 401)

    def test_create_empty_body(self) : 
        req = self.client.post(self.create_playlist_endpoint, headers=self.headers)
        self.assertEqual(req.status_code, 400)
    
    def test_create_success(self) :
        data = {
            'title' : 'test title'
        } 
        req = self.client.post(self.create_playlist_endpoint, data=data,headers=self.headers)
        self.assertEqual(req.status_code, 201)

